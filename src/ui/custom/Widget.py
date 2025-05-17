from PySide6.QtCore import Qt, Signal
from PySide6.QtGui import QMovie, QPixmap
from PySide6.QtWidgets import QLabel, QPushButton


class CustomPushButton(QPushButton):
    # Custom signal to include the mouse button information
    clicked_with_button = Signal(str)

    def mousePressEvent(self, event):  # noqa: N802
        if event.button() == Qt.MouseButton.LeftButton:
            self.clicked_with_button.emit("left")
        elif event.button() == Qt.MouseButton.RightButton:
            self.clicked_with_button.emit("right")
        else:
            self.clicked_with_button.emit("middle")
        super(CustomPushButton, self).mousePressEvent(event)


class CustomLabel(QLabel):
    # Custom signal to include the mouse button information
    clicked_with_button = Signal(str)
    gif_finished = Signal()
    base_font_size: int = -1

    def __init__(self, parent=None):
        super().__init__(parent)
        self.gif = None

    def setText(self, arg__1: str, adjust_size=False, ratio: float = 1) -> None:  # noqa: N802
        """over ride the setText of qt
        if adust_size is true the font is going to get smaller the more charecter it has
        ration determains the curve speed. higher means it is going to get smaller faster. negetive value means its going to get bigger

        :param arg__1: the input text
        :type arg__1: str
        :param adjust_size: change font dynamicly, defaults to False
        :type adjust_size: bool, optional
        :param ratio: how aggresive is the adjustment, defaults to 1
        :type ratio: float, optional
        """
        super().setText(arg__1)
        if not adjust_size:
            return
        font = self.font()
        # Determine the number of characters after ignoring the first n characters
        adjusted_length = max(0, len(arg__1) - 10)

        # Reduce the font size based on the adjusted number of characters
        if adjusted_length > 0:
            font.setPointSize(abs(self.base_font_size - int(len(arg__1) * ratio)))
        else:
            font.setPointSize(self.base_font_size)

        # Apply the updated font
        self.setFont(font, adust_size=False)

    def setFont(self, arg__1, adust_size=True) -> None:  # noqa: N802
        if adust_size:
            self.base_font_size = arg__1.pointSize()
        return super().setFont(arg__1)

    def mousePressEvent(self, event):  # noqa: N802
        if event.button() == Qt.MouseButton.LeftButton:
            self.clicked_with_button.emit("left")
        elif event.button() == Qt.MouseButton.RightButton:
            self.clicked_with_button.emit("right")
        else:
            self.clicked_with_button.emit("middle")
        super(CustomLabel, self).mousePressEvent(event)
