from enum import Enum

from PySide6.QtCore import Qt
from PySide6.QtWidgets import QFileDialog, QMessageBox, QWidget


class MessageBoxButtons(Enum):
    YES_CANCEL = {
        QMessageBox.StandardButton.Yes: "باشه",
        QMessageBox.StandardButton.Cancel: "لغو",
    }
    DEFUALT = {}
    OK = {
        QMessageBox.StandardButton.Ok: "باشه",
    }


def create_message_box(
    parent: QWidget,
    title: str,
    text: str,
    icon: QMessageBox.Icon = QMessageBox.Icon.Information,
    button_texts: MessageBoxButtons = MessageBoxButtons.DEFUALT,
) -> QMessageBox:
    # Create the QMessageBox instance
    message_box = QMessageBox(parent)
    message_box.setWindowTitle(title)
    message_box.setText(text)
    message_box.setIcon(icon)

    for button, text in button_texts.value.items():
        message_box.addButton(button)
        message_box.button(button).setText(text)

    return message_box


def create_open_file_dialog(
    parent: QWidget,
    caption: str = "بازکردن فایل",
    dir_: str = "",
):
    options = QFileDialog.Options()  # type: ignore
    file_name, _ = QFileDialog.getOpenFileName(
        parent,
        caption,
        dir_,
        "PDF (*.pdf);;All Files (*)",
        options=options,
    )
    return file_name


def create_save_file_dialog(
    parent: QWidget,
    caption: str = "ذخیره فایل",
    dir_: str = "",
):
    options = QFileDialog.Options()  # type: ignore
    file_name, _ = QFileDialog.getSaveFileName(
        parent,
        caption,
        dir_,
        "PDF (*.pdf);;All Files (*)",
        options=options,
    )
    return file_name


# Base class that handles the Esc key press event
class CloseableDialog:
    def keyPressEvent(self, event):  # noqa: N802
        if event.key() == Qt.Key.Key_Escape:
            self.close()  # type: ignore # Close the dialog when Esc is pressed
        else:
            super().keyPressEvent(event)  # type: ignore # Handle other key events normally
