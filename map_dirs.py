'''/map_dirs.py'''
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
import shutil
from subprocess import call

def _map(args, conf):
    '''this function creates a mapping of the dirs and an order
    according to depth of subdirs.'''
    start_point = args.start_point
    if not os.path.exists(start_point):
        print '{} is not a valid location.'.format(start_point)
    else:
        start_point = os.path.abspath(start_point)
        if not os.path.isdir(start_point):
            return {os.path.dirname(start_point):{'files':[start_point],'depth':1}}, [start_point]
        else:
            new_file_tree = conf['new_file_tree'].keys()[0]
            if new_file_tree:
                new_file_tree_prefix = conf['new_file_tree'][new_file_tree]['new_file_tree_prefix']
                new_start_point = os.path.join(
                    os.path.split(start_point)[0],
                    new_file_tree_prefix + os.path.split(start_point)[1])
                if os.path.exists(new_start_point):
                    if os.path.isdir(new_start_point):
                        shutil.rmtree(new_start_point)
                    else:
                        os.remove(new_start_point)
                shutil.copytree(start_point, new_start_point)
                print call(['ls','-R',new_start_point])
                start_point = new_start_point
            mapping = {}
            order = []
            #print type(start_point) #debug
            for (path, dirs, files) in os.walk(start_point):
                print str(path)+', '+str(dirs)+', '+str(files) #debug
                mapping[path] = {}
                #mapping[path]['dirs']  = dirs
                mapping[path]['files'] = files
                mapping[path]['depth'] = len(path.split('/'))

            for path in mapping.keys():
                order.append(path)

            order.sort()

            return mapping, order
