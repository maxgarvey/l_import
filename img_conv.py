''' /av_conv.py '''
from subprocess import call
import os

def img_convert(filepath, conf):
    '''this method will convert a file to the format specified in the conf'''
    input_formats = ['.bmp','.art','.bmp2','.bmp3','.cmyk','.cmyka','.dot','.epi','.eps','.fts','.jng','.jpeg','.jpg','.mng','.miff','.otf','.png','.psd','.rgb','.rgba','.svg','.tiff','.yuv']
    output_formats = ['.bmp','.art','.bmp2','.bmp3','.cmyk','.cmyka','.dot','.epi','.eps','.fts','.jng','.jpeg','.jpg','.mng','.miff','.otf','.png','.psd','.rgb','.rgba','.svg','.tiff','.yuv']

    filename, extension = os.path.splitext(filepath)
    if extension.lower() not in input_formats:
        pass

    elif conf['convert_img'].keys()[0]:
        end_format = conf['convert_img'][True]['end_format']
        if end_format not in output_formats:
            print 'desired output format: {} not supported.'.format(end_format)
        else:
            try:
                call(['convert', filepath, filename + end_format])
                try:
                    os.remove(filepath)
                except:
                    pass
            except Exception, err:
                print 'error converting file: {0}, from {1} to {2}'.format(filepath, extension, end_format)
