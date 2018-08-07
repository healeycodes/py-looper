import sys
import pathlib
import multiprocessing
from moviepy.editor import ImageClip, AudioFileClip
from moviepy.audio.fx import audio_loop


# prints custom error regarding command line arguments
def arg_error(err, e=None):
    if e is not None:
        print(e)
    print('Command line argument error.\n')
    print('Error: {0}\n'.format(err))
    print('Required args: [image] [audio] [min_length] [movie_name]')
    print('E.g., my_image.png my_audio.mp3 0.30 my_movie')
    print('Note: [min_length] is formatted as Minutes.Seconds')
    print('Optional ending arg: [location], e.g., \'C:/videos\'')
    input('Quiting..')
    sys.exit(1)


# program entry point
def video_creation():

    # command line arguments [main.py, image, audio, min_length, movie_name]
    if len(sys.argv) < 5:
        arg_error('{0} args supplied but {1} args required.'.format(
            len(sys.argv) - 1, 4))

    location = ''  # default is no location, i.e., save video in working directory
    if len(sys.argv) > 5:
        if len(sys.argv[5]) > 0:  # allow empty path for future compatibility
            location = sys.argv[5]
            # append slash if required
            if location[-1] != '/' and location[-1] != '\\':
                location += '/'
            try:
                # create directory if needed (works recursively)
                pathlib.Path(location).mkdir(parents=True, exist_ok=True)
            except Exception as e:
                arg_error('problem with location \'{0}\'. Either it could not be found or it could not be created.'.format(
                    location), e)

    image_src = sys.argv[1]
    audio_src = sys.argv[2]

    try:
        min_length = int(str(sys.argv[3]).split(  # format: Minutes.Seconds
            '.')[0]) * 60 + int(str(sys.argv[3]).split('.')[1])  # converted to seconds
    except Exception as e:
        arg_error('[min_length] not parsable. \'{0}\' was supplied when the correct format is \'numbers.numbers\', e.g., \'123.59\'.'.format(
            sys.argv[3]), e)

    if min_length < 1:
        min_length = 1  # keep min_length no smaller than one second

    movie_name = sys.argv[4] + '.mp4'

    # beginning of moviepy functions
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
    image_clip.write_videofile(location + movie_name, preset='ultrafast',
                               threads=multiprocessing.cpu_count())


video_creation()  # start program
