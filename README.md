## py-looper
Create MP4 clips from an image and loopable audio, via command line.


### Installation

`ffmpeg` is required but may be installed automatically. https://www.ffmpeg.org/

`pip` is required. https://pip.pypa.io/en/stable/installing/

`cd py-looper`

`pip install -r requirements.txt`


### Running

`cd py-looper`

`python main.py [image] [audio] [min_length] [movie_name]`

Creates `[movie_name].mp4` in the py-looper directory.

e.g., `python main.py my_image.png my_audio.mp3 1.0 my_movie`


#### [image]

Any picture file (png, tiff, jpeg, etc.)

#### [audio]

Any audio file.

#### [min_length]

Formatted as `Minutes.Seconds`. One minute is `1.0`. Thirty seconds is `0.30`. Note: the preceding `0.` is required when specifiying a time less than one minute.

The program will loop the audio file until the resulting video is at least as long as the min_length parameter.

#### [movie_name]

Any string, e.g., `hello`, `test-123`, `'spaces required quotes'`. The file will be saved as MP4.
