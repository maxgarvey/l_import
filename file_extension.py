'''/file_extension.py'''
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

def standardize(name, conf, verbose):
    '''this method will change the file extension to match a standardized format.'''
    mode = conf['file_extensions']
    #try:
    #    base_path  = os.split(name)[0]
    name_base  = name.split('.')[0]
    name_parts = name.split('.')[1:]
    #except Exception, err:
    #    return name

    if verbose or conf['verbose']:
        #print 'base_path: {}'.format(base_path) #debug
        print 'name_base: {}'.format(name_base) #debug
        print 'name_parts: {}'.format(name_parts) #debug

    if mode == 'lowercase':
        index = 0
        for part in name_parts:
            name_parts[index] = name_parts[index].lower()
            index += 1
        if len(name_parts) > 0:
            final_name = '.'.join([name_base,('.'.join(name_parts))])
        else:
            final_name = name_base
        return final_name

    elif mode == 'uppercase':
        index = 0
        for part in name_parts:
            name_parts[index] = name_parts[index].upper()
            index += 1
        if len(name_parts) > 0:
            final_name = '.'.join([name_base,('.'.join(name_parts))])
        else:
            final_name = name_base
        return final_name

    elif mode == 'camelcase':
        index = 0
        for part in name_parts:
            name_parts[index] = name_parts[index].lower()
            name_parts[index] = name_parts[index][0].upper() + name_parts[index][1:]
            index += 1
        if len(name_parts) > 0:
            final_name = '.'.join([name_base,('.'.join(name_parts))])
        else:
            final_name = name_base
        return final_name

    else:
        print 'invalid mode for extension standardization.'
