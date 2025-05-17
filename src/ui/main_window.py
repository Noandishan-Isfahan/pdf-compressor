import shutil
from pathlib import Path

from PySide6.QtCore import Qt
from PySide6.QtGui import QIcon, QPixmap
from PySide6.QtWidgets import QMainWindow

from setting import DEFUALT_COLOR_IMAGE_RES, MAIN_ICON, MAIN_LOGO
from src.services.pdf_compressor.compressor import compress
from src.ui.custom.dialog import (
    create_message_box,
    create_open_file_dialog,
    create_save_file_dialog,
)
from src.ui.forms.main import Ui_mainWindow
from src.utils.file import get_human_readable_size


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setWindowIcon(QIcon(str(MAIN_ICON)))
        self.ui = Ui_mainWindow()
        self.ui.setupUi(self)
        self.set_defaults()
        self.setup_signals()
        self.setup_shortcuts()

    def set_defaults(self):
        self.original_file = None
        self.ui.lbl_file_name.setText("فایلی انتخاب نشده است")
        self.ui.lbl_file_size.setText("0 بایت")

        self.ui.txt_color_image_res.setText(str(DEFUALT_COLOR_IMAGE_RES))
        self.ui.txt_mono_image_res.setText(str(DEFUALT_COLOR_IMAGE_RES))
        self.ui.txt_gray_image_res.setText(str(DEFUALT_COLOR_IMAGE_RES))

        self.ui.lbl_logo.setPixmap(QPixmap(str(MAIN_LOGO)))

    def setup_signals(self):
        self.ui.btn_openfile.clicked.connect(self.btn_openfile_clicked)
        self.ui.menu_openfile.triggered.connect(self.btn_openfile_clicked)
        self.ui.menu_savefile.triggered.connect(self.btn_save_clicked)
        self.ui.btn_convert.clicked.connect(self.btn_compress_clicked)
        self.ui.btn_savefile.clicked.connect(self.btn_save_clicked)

    def setup_shortcuts(self):
        self.ui.menu_openfile.setShortcut("Ctrl+O")
        self.ui.menu_savefile.setShortcut("Ctrl+s")
        self.ui.btn_openfile.setShortcut("Ctrl+t")

    def btn_openfile_clicked(self):
        file_path = create_open_file_dialog(
            self,
            "بازکردن فایل",
        )
        if not file_path:
            return
        file = Path(file_path)
        if not file.exists() or not file.is_file():
            return
        if file.suffix != ".pdf":
            create_message_box(
                self, "فرمت فایل اشتباه", "فرمت فایل باید PDF باشد"
            ).exec()
        self.ui.lbl_file_name.setText(file.name)
        self.ui.lbl_file_size.setText(get_human_readable_size(file))
        self.original_file = file

    def btn_compress_clicked(self):
        if not self.original_file:
            create_message_box(
                self, "فایلی انتخاب نشده", "لطفا یک فایل انتخاب کنید"
            ).exec()
            return
        converted_file = compress(
            int(self.ui.txt_color_image_res.text()),
            int(self.ui.txt_gray_image_res.text()),
            int(self.ui.txt_mono_image_res.text()),
            self.original_file,
        )
        if not converted_file:
            create_message_box(self, "خطا", "فایل فشرده سازی نشد").exec()
            return
        self.converted_file = converted_file
        self.ui.lbl_file_after_size.setText(get_human_readable_size(converted_file))
        create_message_box(self, "موفقیت", "تبدیل با موفقیت انجام شد").exec()

    def btn_save_clicked(self):
        if not self.converted_file:
            create_message_box(
                self, "فایلی انتخاب نشده", "لطفا یک فایل انتخاب کنید"
            ).exec()
            return
        file_path = create_save_file_dialog(
            self,
            "ذخیره فایل",
        )
        if not file_path:
            return
        file = Path(file_path)
        file = file.with_suffix(".pdf")
        shutil.copy(self.converted_file, file)
        create_message_box(self, "موفقیت", "فایل با موفقیت ذخیره شد").exec()
