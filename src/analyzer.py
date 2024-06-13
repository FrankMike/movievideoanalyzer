import os
import re

import cv2


def analyze(path):
    """
    Return movie details
    """
    # Title
    # Extract title from the file path
    title = os.path.basename(re.sub(r"\s*\(.*?\)", "", os.path.splitext(path)[0]))
    print(f"Analyzing {title}")

    # Year
    # Extract year from the file path
    y = re.search(r"\((\d{4})", path)
    year = str(y.group(1) if y else None)

    # File size
    # Get the file size in GB
    file_size = round(os.path.getsize(path) / (1024 * 1024 * 1024), 2)

    # File extension
    # Get the file extension
    file_extension = os.path.splitext(path)[1]

    # Video analysis
    if file_extension in [".mp4", ".mkv"]:
        video = cv2.VideoCapture(path)

        # Video resolution
        width = int(video.get(cv2.CAP_PROP_FRAME_WIDTH))
        height = int(video.get(cv2.CAP_PROP_FRAME_HEIGHT))
        if 3800 < width <= 3840 or height == 2160:
            resolution = "4K"
        elif 1850 < width <= 1920 or height == 1080:
            resolution = "HD 1080p"
        elif width == 1280 or height == 720:
            resolution = "HD 720p"
        elif width < 1200:
            resolution = "SD"
        else:
            resolution = "Unknown"

        # Video resolution size
        resolution_size = f"{width}x{height}"

        # Video codec
        h = int(video.get(cv2.CAP_PROP_FOURCC))
        codec = (
            ""
            + chr(h & 0xFF)
            + chr((h >> 8) & 0xFF)
            + chr((h >> 16) & 0xFF)
            + chr((h >> 24) & 0xFF)
        ).upper()
        if codec == "AV01":
            codec = "AV1"

        video.release()

        # Return the movie model
        return {
            "title": title,
            "year": year,
            "file_size": file_size,
            "resolution": resolution,
            "resolution_size": resolution_size,
            "codec": codec,
        }
