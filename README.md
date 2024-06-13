# Movie Video Analyzer

Python script which extracts and analyzes details of movie video files. The script uses regular expressions for parsing file paths and OpenCV for video file analysis.

## Features

- Extracts movie title from file path.
- Extracts the release year from file path.
- Computes the file size in GB.
- Determines the video resolution (4K, HD 1080p, HD 720p, SD).
- Identifies the video codec used.

## Requirements

- Python 3.x
- OpenCV
- `os` and `re` Python standard libraries

## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/FrankMike/movievideoanalyzer.git
    ```
2. Navigate to the repository directory:
    ```bash
    cd movievideoanalyzer
    ```
3. Install the required Python packages:
    ```bash
    pip install -r requirements.txt
    ```

## Usage

To analyze a movie file, run the `analyze.py` script with the path to the movie file as an argument:

```python
import analyze

# Replace 'path/to/movie/file' with the actual file path
movie_details = analyze("path/to/movie/file")
print(movie_details)
```

## Example

```json
{
    "title": "Inception",
    "year": "2010",
    "file_size": 1.5,  # GB
    "resolution": "HD 1080p",
    "resolution_size": "1920x1080",
    "codec": "H264"
}
```
