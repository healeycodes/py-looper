## py-looper

Create long videos from a loopable audio track and a static image - resulting in a video file that dynamically stretches to never cut off your track :heart:.

<br>

### Pre-installation

python - https://www.python.org. Tested with Python v3.6.5 (and assumed to not work with versions prior to this). Python is packaged with Mac OS X and Linux but not Windows. Check your Python version if you run into issues (`python -v`).

ffmpeg - https://www.ffmpeg.org/ - is required but should be installed automatically if not present. It's also packaged with some OSes and other programs often require it.

pip - https://pip.pypa.io/en/stable/installing/ - is required. It's the standard Python package manager and is sometimes installed when Python is.

<br>

### Installation

Navigate to the py-looper folder via terminal or cmd `cd py-looper`

Install dependencies via `pip install -r requirements.txt`.

<br>

### Running

`cd py-looper`

`python main.py [image] [audio] [min_length] [movie_name]`

e.g., `python main.py my_image.png my_audio.mp3 1.0 my_movie` creates `[movie_name].mp4` in the py-looper directory.

The resulting video file will have the same dimensions as the supplied `[image]`.

Spaces in these arguments will require the argument to be passed with `'` single quote marks on most terminals. E.g., `'My Image File.png'`. Remember you can use tab to autocomplete image/audio filenames and locations.

<br>

#### `[image]`

Any picture file (png, tiff, jpeg, etc.)

#### `[audio]`

Any audio file that loops perfectly.

#### `[min_length]`

Formatted as `Minutes.Seconds`. One minute is `1.0`. Thirty seconds is `0.30`. Note: the preceding `0.` is required when specifiying a time less than one minute.

The program will loop the audio file until the resulting video is at least as long as the min_length parameter.

#### `[movie_name]`

Any string, e.g., `hello` or `test-123`. The file will be saved as MP4.
