''' /av_conv.py '''
'''
Copyright (c) 2012, Max Garvey
All rights reserved.

Redistribution and use in source and binary forms, with or without
modification, are permitted provided that the following conditions are met: 

1. Redistributions of source code must retain the above copyright notice, this
   list of conditions and the following disclaimer. 
2. Redistributions in binary form must reproduce the above copyright notice,
   this list of conditions and the following disclaimer in the documentation
   and/or other materials provided with the distribution. 

THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND
ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT OWNER OR CONTRIBUTORS BE LIABLE FOR
ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES
(INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES;
LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND
ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
(INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS
SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.

The views and conclusions contained in the software and documentation are those
of the authors and should not be interpreted as representing official policies, 
either expressed or implied, of the FreeBSD Project.
'''

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
