import shutil
import subprocess
from pathlib import Path

FILES_TO_MOVE = [
    Path("app.py"),
    Path("setting.py"),
    Path("img"),
    Path("src"),
]
BUILD_DIR = Path("build")
BASE_NAME = "PDF Compressor "
EXECUTABLE_DATA_PATHS = [Path("img")]
EXECUTABLE_ENTRY_POINT = Path("app.py")


def move_files_to_build():  # noqa: C901
    if not BUILD_DIR.exists():
        BUILD_DIR.mkdir(parents=True)
    for item in FILES_TO_MOVE:
        destination = BUILD_DIR / item.name
        if item.is_dir():
            print(f"Copying directory: {item} to {destination}")
            shutil.copytree(item, destination)
        elif item.is_file():
            print(f"Copying file: {item} to {destination}")
            shutil.copy2(item, destination)


def convert_to_executable():
    """
    """
    icon = Path(BUILD_DIR / "img" / "default_images" / "logo.ico")
    if input("Change name ? (Default No)") in ["yes", "Y", "y", "YES"]:
        name = input("Enter full app name (e.g PDF Compressor v1.6):")
    else:
        name = BASE_NAME + input("Enter Version (e.g V1.6):")
    command = "pyinstaller --noconfirm --onefile --windowed "
    command += f'--icon "{str(icon.absolute())}" '
    command += f'--name "{name.strip()}" '
    for d in EXECUTABLE_DATA_PATHS:
        command += rf'--add-data "{str((BUILD_DIR/d).absolute())}:{d.name}/" '
    command += f'"{str((BUILD_DIR/EXECUTABLE_ENTRY_POINT).absolute())}"'
    print(command)
    subprocess.run(command, shell=True)  # noqa: S602, S603


if __name__ == "__main__":
    move_files_to_build()
    convert_to_executable()
