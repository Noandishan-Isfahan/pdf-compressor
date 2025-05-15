from PySide6.QtGui import QIcon
from PySide6.QtWidgets import QMainWindow

from setting import MAIN_ICON

from .forms.main import Ui_mainWindow


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setWindowIcon(QIcon(str(MAIN_ICON)))
        self.ui = Ui_mainWindow()
        self.ui.setupUi(self)

        self.setup_signals()
        self.setup_shortcuts()

    def setup_signals(self):
        self.ui.btn_openfile.clicked.connect(self.btn_openfile_clicked)
        self.ui.menu_openfile.triggered.connect(self.btn_openfile_clicked)

    def setup_shortcuts(self):
        self.ui.menu_openfile.setShortcut("Ctrl+O")
        self.ui.menu_savefile.setShortcut("Ctrl+s")
        self.ui.btn_openfile.setShortcut("Ctrl+t")
    def btn_openfile_clicked(self):
        print("open file")
