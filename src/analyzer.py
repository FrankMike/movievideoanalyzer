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
    year = str(y.group(1)) if y else None

    # File size
    # Get the file size in GB
    try:
        file_size = round(os.path.getsize(path) / (1024 * 1024 * 1024), 2)
    except OSError as e:
        print(f"Error getting file size: {e}")
        file_size = None

    # File extension
    # Get the file extension
    file_extension = os.path.splitext(path)[1].lower()

    # Video analysis
    if file_extension in [".mp4", ".mkv"]:
        try:
            video = cv2.VideoCapture(path)
            if not video.isOpened():
                raise ValueError(f"Error opening video file: {path}")

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
            codec = "".join(chr((h >> (8 * i)) & 0xFF) for i in range(4)).upper()
            codec = "AV1" if codec == "AV01" else codec

        except Exception as e:
            print(f"Error analyzing video: {e}")
            resolution = "Unknown"
            resolution_size = "Unknown"
            codec = "Unknown"
        finally:
            video.release()
    else:
        resolution = "Unknown"
        resolution_size = "Unknown"
        codec = "Unknown"

    # Return the movie model
    return {
        "title": title,
        "year": year,
        "file_size": file_size,
        "resolution": resolution,
        "resolution_size": resolution_size,
        "codec": codec,
    }
