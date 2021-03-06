#!/usr/bin/python
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
from conf import *
from file_extension import *
from map_dirs import *
from name_change import *
from new_name import *
from argparse import ArgumentParser
import os

if __name__ == "__main__":
    '''the main method. with argparse'''
    parser = ArgumentParser()
    parser.add_argument('start_point', action='store', metavar='<START_POINT>', help='the file or directory to convert (recursively).')
    parser.add_argument('-o', dest='output_location', action='store', metavar='<OUTPUT_LOCATION>', default='', help='the location of the resulting dir/files.')
    parser.add_argument('-v', dest='verbose', action='store_true', default=conf['verbose'], help='toggle_verbosity.')
    parser.add_argument('-c', dest='conf_file', action='store', default=os.path.join(os.getcwd(),'conf.py'), metavar='<CONF_FILE>', help='the location of the conf file you want to use.')

    args = parser.parse_args()

    if args.conf_file != os.path.join(os.getcwd(),'conf.py'):
        cwd = os.getcwd()
        try:
            conf_dir, conf_filename = os.path.split(args.conf_file)
            os.chdir(conf_dir)
            from conf import *
        except Exception, err:
            print 'error parsing conf file: {0}\n\t{1}'.format(Exception, err)
        finally:
            os.chdir(cwd)

    if args.verbose:
        conf['verbose'] = True

    if conf['verbose']:
        print 'args:{0}\nconf{1}'.format(args, conf)

    change_names(args, conf)
