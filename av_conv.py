''' /av_conv.py '''
from subprocess import call
import os

def convert(filepath, conf):
    '''this method will convert a file to the format specified in the conf'''
    input_formats = ['.aac','.ac3','.aiff','.alsa','.wav','.swf','.spdif','.rm','.mp3','.avi','.ogg','.oma','.oss','.mov','.mp4','.m4a','.mjpeg','.mkv','m4v','.h264']
    output_formats = ['.aiff','.alsa','.wav','.webm','.swf','.vcd','.spdif','.avi','.rm','.mp3','.mp4','.ogg','.oma','.oss','.mov','.mjpeg','mkv','m4v','h264','gif']

    filename, extension = os.path.splitext(filepath)
    if extension not in input_formats:
        pass

    elif conf['convert_audio'].keys()[0]:
        end_format = conf['convert_audio'][True]['end_format']
        if end_format not in output_formats:
            print 'desired output format: {} not supported.'.format(end_format)
        else:
            try:
                call(['ffmpeg', '-i', filepath, filename + end_format])
                os.remove(filepath)
            except Exception, err:
                print 'error converting file: {0}, from {1} to {2}'.format(filepath, extension, end_format)
