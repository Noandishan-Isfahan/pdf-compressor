from PySide6.QtCore import Qt


# Base class that handles the Esc key press event
class CloseableDialog:
    def keyPressEvent(self, event):  # noqa: N802
        if event.key() == Qt.Key.Key_Escape:
            self.close()  # type: ignore # Close the dialog when Esc is pressed
        else:
            super().keyPressEvent(event)  # type: ignore # Handle other key events normally
