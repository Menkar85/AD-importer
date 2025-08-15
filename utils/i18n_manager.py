from PySide6.QtCore import QTranslator, QLocale, QLibraryInfo


class I18nManager:
    def __init__(self, app):
        self.app = app
        self.translator = QTranslator()
        self.default_translator = QTranslator()
        self.install_system_translations()

    def install_system_translations(self):
        qt_translator = QTranslator()
        if qt_translator.load(
                QLocale(),
                'qtbase',
                '_',
                QLibraryInfo.path(QLibraryInfo.LibraryPath.TranslationsPath)
        ):
            self.app.installTranslator(qt_translator)

    def load_translations(self, lang_code):
        self.app.removeTranslator(self.translator)

        qm_file = f"translations/i18n_{lang_code}.qm"
        if self.translator.load(qm_file):
            self.app.installTranslator(self.translator)
            return True
        return False
