from pathlib import Path
import tempfile

from setting import TEMP_FOLDER


def get_human_readable_size(file_path: Path) -> str:
    size_bytes = file_path.stat().st_size
    for unit in ["B", "KB", "MB"]:
        if size_bytes < 1024:
            return f"{size_bytes:.2f} {unit}"
        size_bytes /= 1024
    return f"{size_bytes:.2f} GB"


def get_temp_file():
    """generates a temporary file path in the temp directory"""

    file = TEMP_FOLDER / "temp.pdf"
    file.touch(exist_ok=True)
    return file
