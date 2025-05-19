import logging
import logging.handlers
import sys
from pathlib import Path

from PySide6.QtCore import QtMsgType, qInstallMessageHandler

if getattr(sys, "frozen", False) and hasattr(sys, "_MEIPASS"):
    ROOT_DIR = Path(sys._MEIPASS)  # type: ignore # For PyInstaller
else:
    ROOT_DIR = Path(__file__).parent
FONT_DIR = ROOT_DIR / "img" / "fonts"
FONT_NAMES = ["Vazirmatn-Regular.ttf"]
FONTS = [str(FONT_DIR / font) for font in FONT_NAMES]

TEMP_FOLDER = ROOT_DIR / "temp"

MAIN_ICON = ROOT_DIR / "img" / "default_images" / "nhs-logo.ico"
MAIN_LOGO = ROOT_DIR / "img" / "default_images" / "nhs-logo.png"

DEFAULT_COLOR_IMAGE_RES = 125
DEFAULT_GRAY_IMAGE_RES = 115
DEFAULT_MONO_IMAGE_RES = 150


LOG_FILENAME = ROOT_DIR / "logs" / "app.log"
if not LOG_FILENAME.parent.exists():
    LOG_FILENAME.parent.mkdir(parents=True, exist_ok=True)
    LOG_FILENAME.touch()
# Configure logging
LOG_LEVEL = logging.DEBUG  # Change to INFO, WARNING, etc. as needed
LOG_FORMAT = "%(asctime)s - %(levelname)s - %(name)s - %(message)s"

# Set up rotating file handler (Size-based rotation)
file_handler = logging.handlers.RotatingFileHandler(
    LOG_FILENAME, maxBytes=5 * 1024 * 1024, backupCount=5, encoding="utf-8"
)

file_handler.setLevel(LOG_LEVEL)
file_handler.setFormatter(logging.Formatter(LOG_FORMAT))

# Set up console handler
console_handler = logging.StreamHandler()
console_handler.setLevel(logging.INFO)  # Console can have a different log level
console_handler.setFormatter(logging.Formatter(LOG_FORMAT))

# Configure root logger
logging.basicConfig(level=LOG_LEVEL, handlers=[file_handler, console_handler])


# === Integrate PySide6 logging ===
def qt_message_handler(mode, context, message):
    """Redirect Qt logging to Python's logging module."""
    if mode == QtMsgType.QtDebugMsg:
        logging.debug(f"QtDebug: {message}")
    elif mode == QtMsgType.QtInfoMsg:
        logging.info(f"QtInfo: {message}")
    elif mode == QtMsgType.QtWarningMsg:
        logging.warning(f"QtWarning: {message}")
    elif mode == QtMsgType.QtCriticalMsg:
        logging.error(f"QtCritical: {message}")
    elif mode == QtMsgType.QtFatalMsg:
        logging.critical(f"QtFatal: {message}")


# Install the message handler
qInstallMessageHandler(qt_message_handler)


# === Capture Uncaught Exceptions ===
def handle_uncaught_exception(exc_type, exc_value, exc_traceback):
    """Log uncaught exceptions instead of printing them to stderr."""
    if issubclass(exc_type, KeyboardInterrupt):
        # Let KeyboardInterrupt exit the program without logging
        sys.__excepthook__(exc_type, exc_value, exc_traceback)
        return
    logging.critical(
        "Uncaught Exception", exc_info=(exc_type, exc_value, exc_traceback)
    )


# Install exception hook
sys.excepthook = handle_uncaught_exception
