# Video Editing Script with MoviePy

This Python script uses the `moviepy` library to add a text overlay to the first 30 seconds of a video file. The resulting video is saved as a new file.

## Prerequisites

Ensure you have the following installed:

- Python 3.x
- `moviepy` library

You can install `moviepy` using pip:

```sh
pip install moviepy
```
## Usage
1. Place your video file named demo.mp4 in the same directory as the script.
2. Run the script:
```sh
python inedx.py
```
## Script Overview
The script performs the following steps:

* Loads `demo.mp4`.
* Extracts the first 30 seconds of the video.
* Adds a text overlay ("enjoy world!") at the center of the video.
* Combines the original video clip and the text overlay into a single video.
* Saves the resulting video as `enjoy.mp4`.
## Acknowledgments
* `MoviePy` - Used for video editing.

# Happy Coding!
