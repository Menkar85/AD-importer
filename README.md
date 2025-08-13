### AD Importer – Batch user creation for Active Directory

[![Python](https://img.shields.io/badge/Python-3.10+-blue.svg)](https://www.python.org/downloads/)
[![License: GPL v3](https://img.shields.io/badge/License-GPLv3-green.svg)](LICENSE)
[![GitHub stars](https://img.shields.io/github/stars/menkar85/ADuser_batch_add)](https://github.com/menkar85/AD-importer/stargazers)
[![Version](https://img.shields.io/badge/version-0.0.1-green.svg)](https://github.com/menkar85/AD-importer/releases)

A lightweight PySide6 desktop tool to import many users into Active Directory from an Excel file. It previews your data, creates missing OUs, and writes a result workbook showing per-user status and errors.

### Features-

- **GUI workflow**: Simple PySide6 interface; no need for PowerShell scripting
- **Excel import**: Reads XLSX; ready-to-use template included (`Import template.xlsx`)
- **UPN/email generation**: Usernames transliterated (RU→EN) and combined with your UPN suffix
- **OU auto-creation**: Creates nested OUs in the target path if they don’t exist
- **Result workbook**: Exports a new XLSX with success flag and error message per row
- **Protocol choice**: LDAP and LDAPS supported (configurable in Settings)
- **Settings persistence**: Optionally keep last-used AD settings between runs

### Prerequisites

- Windows with network access to your AD domain
- Account with permissions to create users and OUs
- If using LDAPS, a properly configured AD certificate

### Installation

1) Download Zip-archive from the release section
2) Unzip into destination folder
3) Start application with ad-importer.exe file
4) Follow **usage** section below

### Usage

1) In the top panel, fill in:
- **AD Server name**: e.g. `dc.company.local`
- **User name**: e.g. `administrator@company.local`
- **Password**
- **UPN-suffix**: e.g. `company.local` (used to form `userPrincipalName` and email domain)

2) In the Import configuration panel:
- **Source file**: Pick your XLSX or start from `Import template.xlsx`
- **Destination OU**: Use folder-style path with `/` as separators, e.g. `Users/Staff/Engineering`
- **Save result to**: Choose where the result XLSX will be written

3) Optional actions:
- Click **Test** to validate that the AD server name resolves
- Click **Preview file** to inspect the XLSX content before import

4) Click **Start importing** and confirm.

When finished, the app shows a summary and loads the result file into the preview table.

### Settings

Open via menu: `Settings → Settings`

- **Log folder**: Choose a folder to store logs (future use)
- **Keep Active Directory configuration on application close**: Reuse last values next run
- **Protocol**: Select LDAP or LDAPS

### Excel template

Use the included `Import template.xlsx` or prepare your own file with columns in this order:

| Column | Field              | Required | Notes |
|-------:|--------------------|----------|-------|
| A      | Given name         | Yes      | Used for `givenName` and display name |
| B      | Surname            | Yes      | Transliterated to build the login/`cn` |
| C      | Suffix (optional)  | No       | Appended to login/`cn` (e.g., year/group) |
| D      | Password           | Yes      | Initial password; users will be forced to change at first login |
| E      | Phone              | No       | Stored in `telephoneNumber` |
| F      | Description        | No       | Stored in `description` |

During import the app generates and assigns:
- `cn` and login part: transliterated Surname + optional Suffix (Column C)
- `displayName`: `Given name + Surname`
- `userPrincipalName`: `cn@<UPN-suffix>`
- `mail`: `cn@<UPN-suffix>` (email domain follows the UPN suffix)

### OU path format

Specify OUs as a path using `/`:

```text
Users                → OU=Users,DC=company,DC=local
Users/Staff          → OU=Staff,OU=Users,DC=company,DC=local
Departments/IT/Dev   → OU=Dev,OU=IT,OU=Departments,DC=company,DC=local
```

Missing OUs in the path are created automatically.

### Result workbook

After processing, a result XLSX is written to the location you chose. It contains:
- All original/generated user fields
- Extra columns:
  - `done`: `Y` on success, `N` on failure
  - `errors`: error text if creation failed

Note: Existing accounts are detected and reported. Review the `errors` column in the result file for details.

### Project structure

```text
AD-importer/
  main.py                  # App entry point (PySide6)
  mainwindow.py            # Main window logic and workflow
  settings.py              # Settings dialog behavior and persistence
  ui_mainwindow.py         # Generated UI (do not edit manually)
  ui_settings.py           # Generated UI (do not edit manually)
  utils/
    ad_utils.py            # AD operations (pyad), OU creation, user creation
    xlsxutils.py           # XLSX read/build/write helpers
  Import template.xlsx     # Sample/template for input data
  LICENSE                  # GPL-3.0
  requirements.txt         # Python dependencies
```

### Troubleshooting

- Cannot resolve server name: use the **Test** button; verify DNS and domain connectivity
- Authentication/permission errors: ensure the account can create users and OUs in the target
- LDAPS errors: verify certificates and LDAPS configuration on the domain controllers
- Excel parsing errors: ensure your file is `.xlsx` and follows the column order above
- Duplicate/Existing users: check the result file `errors` column, adjust the source XLSX if needed

### Security

- Prefer LDAPS in production
- Handle credentials securely; avoid committing them to files
- Test in a non-production OU first

### License

GPL-3.0. See `LICENSE` for details.

### Version

`0.0.1-alpha`

### Contributing

Issues and pull requests are welcome.
