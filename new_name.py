'''/new_name.py'''
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

import os

def linux_name(full_filepath, conf):
    mode = conf['filenames']
    '''this method will take an existing filename and return the
    linuxized filename camelcase or underscored'''

    l_basepath = os.path.split(full_filepath)[0]
    existing_filename = os.path.split(full_filepath)[1]
    l_filename = ''

    #camelcase
    if mode != 'camelcase':
        l_filename = existing_filename.replace('\\ ','_').replace(' ','_')
    else:
        position = 0
        positions = []
        not_done = True

        while not_done:
            try:
                position = existing_filename.index('\ ')
                existing_filename = existing_filename[:position] + \
                    existing_filename[(position+2):(position+3)].upper() + \
                    existing_filename[(position+3):]
            except ValueError, err:
                not_done = False

        not_done = True
        while not_done:
            try:
                position = existing_filename.index(' ')
                existing_filename = existing_filename[:position] + \
                    existing_filename[(position+1):(position+2)].upper() + \
                    existing_filename[(position+2):]
            except ValueError, err:
                not_done = False

        l_filename = existing_filename

    #lowercase with underscores
    if mode == 'lc_underscore':
        try:
            l_filename = l_filename[:l_filename.rindex('.')].lower() + l_filename[l_filename.rindex('.'):]
        except Exception, err:
            l_filename = l_filename.lower()

    #uppercase with underscores
    if mode == 'uc_underscore':
        try:
            l_filename = l_filename[:l_filename.rindex('.')].upper() + l_filename[l_filename.rindex('.'):]
        except Exception, err:
            l_filename = l_filename.upper()
       

    return os.path.join(l_basepath, l_filename)
