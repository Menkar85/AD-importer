# AD Importer – Batch User Creation for Active Directory

[![Python](https://img.shields.io/badge/Python-3.10+-blue.svg)](https://www.python.org/downloads/)
[![License: GPL v3](https://img.shields.io/badge/License-GPLv3-green.svg)](LICENSE)
[![GitHub stars](https://img.shields.io/github/stars/menkar85/AD-importer)](https://github.com/menkar85/AD-importer/stargazers)
[![Version](https://img.shields.io/badge/version-0.1.2-green.svg)](https://github.com/menkar85/AD-importer/releases)

A lightweight PySide6 desktop application for batch user creation in Active Directory. Import users from Excel files with automatic OU creation, username transliteration (Russian→English), and comprehensive result reporting.

## ✨ Features

- **Intuitive GUI**: Easy-to-use PySide6 interface - no PowerShell scripting required
- **Excel Integration**: Import from XLSX files with included template (`Import template.xlsx`)
- **Smart Username Generation**: Automatic transliteration (RU→EN) and UPN/email creation
- **OU Management**: Automatic creation of nested Organizational Units
- **Detailed Results**: Export comprehensive XLSX with success/failure status and error messages
- **Flexible Protocols**: Support for both LDAP and LDAPS connections
- **Persistent Settings**: Save and reuse Active Directory configuration between sessions
- **Multi-language UI**: English and Russian; switch via menu and restart the app to apply
- **Password Policy**: New users are set to change password at first login automatically

## 📋 Prerequisites

- **Windows OS** with network access to your Active Directory domain
- **AD Account** with permissions to create users and Organizational Units
- **LDAPS Certificate** (if using LDAPS protocol)
- **Python 3.10+** (for development/compilation)

## 🚀 Installation

### For End Users

1. Download the latest release ZIP archive from the [Releases](https://github.com/menkar85/AD-importer/releases) section
2. Extract the ZIP file to your desired location
3. Run the `ad-importer.exe` application
4. Follow the usage instructions below

### For Developers

```bash
# Clone the repository
git clone https://github.com/menkar85/AD-importer.git
cd AD-importer

# Create and activate virtual environment
python -m venv .venv
# Windows (PowerShell)
.venv\Scripts\Activate.ps1
# Windows (cmd)
.venv\Scripts\activate.bat

# Install dependencies
pip install -r requirements.txt

# Run the application
python main.py
```

## 💻 Usage Guide

### Quick Start

1. **Configure Active Directory Connection**:

   - **AD Server**: Enter your domain controller (e.g., `dc.company.local`)
   - **Username**: Provide your AD account (e.g., `administrator@company.local`)
   - **Password**: Enter your AD password
   - **UPN Suffix**: Specify your UPN domain (e.g., `company.local`)
   - **Email domain**: Specify e-mail domain which will be appended for created users(e.g., `mail.company.local`)

2. **Configure Import Settings**:

   - **Source File**: Select your Excel file or use the provided template
   - **Destination OU**: Set target path using `/` separators (e.g., `Users/Staff/Engineering`)
   - **Result File**: Choose output location for the results workbook

3. **Validate Configuration**:

   - Click **Test** to verify AD server connectivity
   - Click **Preview File** to inspect your Excel data

4. **Start Import**:
   - Click **Start Importing** and confirm the operation
   - Review the summary and results when complete

### Step-by-Step Walkthrough

```text
1. Launch AD Importer
2. Enter AD server credentials and UPN suffix
3. Browse and select your Excel source file
4. Set destination OU path (e.g., "Users/Department/Team")
5. Choose save location for results file
6. Test connection to ensure everything works
7. Preview your data to verify format
8. Start the import process
9. Review results and error messages
```

## ⚙️ Settings

Access settings from the application menu.

### Available Options

- **Log Folder**: Configure directory for application logs
- **Persistent AD Config**: Save Active Directory settings between application sessions
- **Connection Protocol**: Choose between LDAP and LDAPS for AD communication

## 🌐 Localization

- The UI supports English and Russian.
- Switch language from the menu bar (English/Russian actions).
- A restart is required to apply the language change.
- Translation files live in `translations/` (e.g., `i18n_en.qm`, `i18n_ru.qm`).

## 📊 Excel Template Format

### Template Structure

Use the provided `Import template.xlsx` or create your own with the following column structure:

| Column | Field Name        | Required | Description                                               |
| ------ | ----------------- | -------- | --------------------------------------------------------- |
| A      | Given name        | Yes      | User's first name (used for `givenName` and display name) |
| B      | Family Name       | Yes      | User's surname (transliterated to build login name)       |
| C      | Username modifier | Optional | Suffix appended to login name (e.g., year, department)    |
| D      | Password          | Yes      | Initial password (users will change on first login)       |
| E      | Phone number      | Optional | Telephone number stored in `telephoneNumber` attribute    |
| F      | Description       | Optional | User description stored in AD `description` field         |

### Generated Fields

During import, the application automatically generates:

- **Common Name (cn)**: `transliterated_Surname + optional_suffix`
- **Display Name**: `Given name + Family Name`
- **User Principal Name**: `cn@<UPN_suffix>`
- **Email Address**: `cn@<email_domain>` (UPN will be used if no email_domain provided)

### Example Template

```excel
Given name    | Family Name | Username modifier | Password    | Phone number | Description
-------------|-------------|-------------------|-------------|--------------|-------------
John         | Smith       |                   | 123456Qwe!@ | 89053335544  |
Izchek       | Azimov      |                   | 112233!2Qwe | 89994445522  | Dept Leader
Janush       | Batikovs    |                   | 332211Qwer12$| 89655554123  |
```

## 🏢 Organizational Unit (OU) Path Format

### Path Syntax

Use forward slashes (`/`) to specify nested OU paths:

```text
Simple OU:           Users                → OU=Users,DC=company,DC=local
Two-level OU:        Users/Staff          → OU=Staff,OU=Users,DC=company,DC=local
Multi-level OU:      Departments/IT/Dev   → OU=Dev,OU=IT,OU=Departments,DC=company,DC=local
```

### Automatic OU Creation

The application automatically creates any missing OUs in the specified path hierarchy. For example, if you specify `Departments/IT/Dev` but only `Departments` exists, the tool will create both `IT` and `Dev` OUs under it.

## 📈 Result Workbook

### Output Structure

After processing completes, a results XLSX file is generated at your specified location containing:

- **Source Fields**: Given name, Family Name, Password, Phone number, Description
- **Generated Fields**: `cn`, `displayName`, `userPrincipalName`, `mail`, plus other computed attributes
- **Status Columns**:
  - `done`: `Y` for successful creation, `N` for failed creation
  - `errors`: Detailed error message if creation failed
  
Note: The results file includes the Password column. Handle and store it securely.

### Duplicate Account Handling

The application identifies and reports any accounts that already exist. For details on failed imports, including duplicate accounts, refer to the `errors` column in the result file. To ensure idempotency, accounts found in the target OU are treated as already present during import. For accurate duplicate tracking, it is recommended to use a new, non-existent OU on the first import run.

### Example Result

```excel
Given name | Family Name | ... | done | errors
----------|-------------|-----|------|--------
John      | Smith       | ... | Y    | -
Izchek    | Azimov      | ... | N    | User already exists
Janush    | Batikovs    | ... | Y    | -
```

## 📁 Project Structure

```
AD-importer/
├── main.py                    # Application entry point (PySide6)
├── mainwindow.py              # Main window logic and workflow management
├── settings.py                # Settings dialog behavior and persistence
├── ui_mainwindow.py           # Generated UI code (do not edit manually)
├── ui_settings.py             # Generated UI code (do not edit manually)
├── utils/
│   ├── __init__.py            # Package initialization
│   ├── ad_utils.py            # Active Directory operations (pyad integration)
│   ├── i18n_manager.py        # Application translations loader
│   └── xlsxutils.py           # Excel file processing utilities
├── translations/              # Qt translation files (i18n_en.qm, i18n_ru.qm)
├── Import template.xlsx       # Ready-to-use template for input data
├── LICENSE                    # GPL-3.0 license file
├── requirements.txt           # Python dependencies
├── .venv/                     # Virtual environment (development)
└── logs/                      # Application logs directory
```

## 🔧 Troubleshooting

### Common Issues

| Issue                          | Solution                                                             |
| ------------------------------ | -------------------------------------------------------------------- |
| **Cannot resolve server name** | Use the **Test** button; verify DNS and network connectivity         |
| **Authentication failed**      | Check AD account permissions and password accuracy                   |
| **Permission denied**          | Ensure account has rights to create users and OUs in target location |
| **LDAPS connection errors**    | Verify AD certificate configuration and LDAPS setup                  |
| **Excel parsing failures**     | Ensure file is `.xlsx` format and follows column order               |
| **Duplicate user errors**      | Check result file `errors` column; modify source data as needed      |

### Connection Problems

1. **Test connectivity** using the built-in Test button
2. **Verify network access** to domain controllers
3. **Check firewall settings** for LDAP/LDAPS ports (389/636)
4. **Validate DNS resolution** for your AD server

### Performance Tips

- Test imports in a **non-production OU** first
- Process **large files in batches** if performance issues occur
- Monitor **AD server resources** during bulk operations
- Use **LDAPS** for secure production environments

## 🔒 Security Best Practices

### Connection Security

- **Always use LDAPS** in production environments for encrypted communication
- **Validate AD certificates** to prevent man-in-the-middle attacks
- **Use least privilege principle** for AD service accounts

### Data Protection

- **Never hardcode credentials** in configuration files
- **Clear passwords from memory** after authentication
- **Store logs securely** with access controls
- **Test in isolated environments** before production use
- **Treat results XLSX as sensitive** since it contains initial passwords; delete or secure it after use

### Operational Security

- **Regular audit** of created users and permissions
- **Monitor import logs** for suspicious activity
- **Maintain backup** of AD before bulk operations
- **Document standard procedures** for user creation workflows

## 📄 License

This project is licensed under the **GNU General Public License v3.0**. See the [LICENSE](LICENSE) file for full details.

## 🤝 Contributing

We welcome contributions! Please follow these guidelines:

### Development Setup

1. Fork the repository
2. Create a feature branch: `git checkout -b feature/amazing-feature`
3. Make your changes and test thoroughly
4. Commit your changes: `git commit -m 'Add amazing feature'`
5. Push to the branch: `git push origin feature/amazing-feature`
6. Open a Pull Request

### Reporting Issues

- Use the **GitHub Issues** tab to report bugs
- Provide **detailed reproduction steps**
- Include **environment information** (OS, Python version, AD version)
- Attach **log files** and **sample data** when possible

### Code Standards

- Follow **PEP 8** Python style guidelines
- Add **comments** for complex logic
- Include **docstrings** for functions and classes
- **Test your changes** before submitting

---

**AD Importer** - Streamlining Active Directory user management with simplicity and power.
