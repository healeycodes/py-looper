import sys
import multiprocessing
from moviepy.editor import ImageClip, AudioFileClip
from moviepy.audio.fx import audio_loop

# command line arguments [0, image, audio, min_length, movie_name]
try:
    image_src = sys.argv[1]
    audio_src = sys.argv[2]
    min_length = int(str(sys.argv[3]).split(  # format: Minutes.Seconds
        '.')[0]) * 60 + int(str(sys.argv[3]).split('.')[1])  # converted to seconds

    if min_length < 1:
        min_length = 1  # keep min_length no smaller than one second

    movie_name = sys.argv[4] + '.mp4'
except:
    print('Error: Wrong or missing command line arguments!')
    print('[image] [audio] [min_length] [movie_name]')
    print('Example args: my_image.png my_audio.mp3 0.30 my_movie')
    print('[min_length] is formatted as Minutes.Seconds')
    input('All args are required. Quiting..')
    sys.exit(1)

image_clip = ImageClip(image_src)  # get image
audio = AudioFileClip(audio_src)  # get audio

# how many complete audio loops are needed to meet the min_length?
loops_needed = int(min_length / audio.duration + 1)

# loop our audio to meet the min_length
audio = audio_loop.audio_loop(audio, nloops=loops_needed)

# set up our clip
image_clip = image_clip.set_audio(audio)
image_clip.fps = 24
image_clip.duration = audio.duration

# render!
image_clip.write_videofile(movie_name, preset='ultrafast',
                           threads=multiprocessing.cpu_count())
