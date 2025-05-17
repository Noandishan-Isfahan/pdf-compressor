import shutil
import sys
from pathlib import Path

from PySide6.QtGui import QFontDatabase
from PySide6.QtWidgets import (
    QApplication,
)

from setting import FONTS, TEMP_FOLDER
from src.ui.main_window import MainWindow


def main():
    shutil.rmtree(TEMP_FOLDER, ignore_errors=True)
    TEMP_FOLDER.mkdir(parents=True, exist_ok=True)
    app = QApplication(sys.argv)
    app.setStyle("Fusion")
    for font in FONTS:
        QFontDatabase.addApplicationFont(font)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
