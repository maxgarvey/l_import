''' /av_conv.py '''
from subprocess import call
import os

def word_convert(filepath, conf):
    '''this method will convert a file to the format specified in the conf'''
    input_formats = ['.doc','.docx','.abw','.awt','.zabw','.rtf','.odt','.odf']
    output_formats = ['.doc','.docx','.abw','.awt','.zabw','.rtf','.odt','.odf']

    filename, extension = os.path.splitext(filepath)
    if extension.lower() not in input_formats:
        pass

    elif conf['convert_word'].keys()[0]:
        end_format = conf['convert_word'][True]['end_format']
        if end_format not in output_formats:
            print 'desired output format: {} not supported.'.format(end_format)
        else:
            try:
                call(['abiword', '--to={}'.format(end_format[1:]), filepath])
                try:
                    os.remove(filepath)
                except:
                    pass
            except Exception, err:
                print 'error converting file: {0}, from {1} to {2}'.format(filepath, extension, end_format)
