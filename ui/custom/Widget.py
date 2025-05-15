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

    def set_image_or_gif(self, image_path: str, scaled=False):
        # Stop any active movie (if it's a GIF)
        if self.gif and self.gif.state() == QMovie.MovieState.Running:
            self.gif.stop()

        # Determine if the file is a GIF or a static image
        if image_path.lower().endswith(".gif"):
            self.set_gif(image_path)
        else:
            self.set_static_image(image_path, scaled)

    def set_gif(self, gif_path):
        self.gif = QMovie(gif_path)
        self.gif.setScaledSize(self.size())
        self.gif.frameChanged.connect(self.check_if_finished)
        self.setMovie(self.gif)
        self.gif.start()

    def check_if_finished(self, frame_number):
        if frame_number == self.gif.frameCount() - 1:  # type: ignore
            # Emit signal when the last frame is reached
            self.gif_finished.emit()

    def set_static_image(self, image_path, sclaed=False):
        pixmap = QPixmap(image_path)
        self.setPixmap(
            pixmap
            if not sclaed
            else pixmap.scaled(
                self.size(),
                Qt.AspectRatioMode.KeepAspectRatio,
                Qt.TransformationMode.SmoothTransformation,
            )
        )
