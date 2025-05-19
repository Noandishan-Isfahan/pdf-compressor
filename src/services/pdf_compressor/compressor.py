import locale
import sys
from pathlib import Path

import ghostscript

from src.utils.file import get_temp_file


def compress(color_res: int, mono_res: int, gray_res: int, input_file: Path) -> Path:
    """
    Compress a PDF file using Ghostscript with specified downsampling resolutions.

    :param color_res: Color image resolution (e.g. 125)
    :param mono_res: Monochrome image resolution (e.g. 150)
    :param gray_res: Grayscale image resolution (e.g. 115)
    :param input_file: Path to the input PDF file

    :return: Path to the compressed temporary PDF file
    """
    temp_file = get_temp_file()

    gs_cmd = [
        "gs",
        "-sDEVICE=pdfwrite",
        "-dCompatibilityLevel=1.4",
        "-dDownsampleColorImages=true",
        "-dColorImageDownsampleType=/Bicubic",
        f"-dColorImageResolution={color_res}",
        "-dDownsampleGrayImages=true",
        "-dGrayImageDownsampleType=/Bicubic",
        f"-dGrayImageResolution={gray_res}",
        "-dDownsampleMonoImages=true",
        "-dMonoImageDownsampleType=/Subsample",
        f"-dMonoImageResolution={mono_res}",
        "-dDetectDuplicateImages=true",
        "-dNOPAUSE",
        "-dQUIET",
        "-dBATCH",
        f"-sOutputFile={temp_file}",
        str(input_file),
    ]

    ghostscript.Ghostscript(*gs_cmd)
    return temp_file
