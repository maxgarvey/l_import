'''/name_change.py'''
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

from map_dirs import _map
from new_name import linux_name
from file_extension import standardize
from av_conv import convert
from pdf_conv import ps_convert
from img_conv import img_convert
import os
import shutil

def change_names(args, conf):
    '''this method will take a starting point and change all
    the names to more linux friendly ones'''
    dir_map, ordering = _map(args, conf)
    if args.verbose or conf['verbose']:
        print 'dir_map: {}'.format(dir_map)
        print 'ordering: {}'.format(ordering)
    while len(ordering) > 0:
        my_pop = ordering.pop()
        if args.verbose or conf['verbose']:
            print '\npopped: ' + my_pop #debug
            print 'dir_map["' + my_pop + '"]["files"]: ' + str(dir_map[my_pop]["files"]) #debug
        for _file in dir_map[my_pop]["files"]:
            if args.verbose or conf['verbose']:
                print 'file:{}'.format(_file)
            change_this_file = True
            for extension in conf['formats_don\'t_touch']:
                if _file.endswith(extension):
                    change_this_file = False
            if change_this_file:
                if args.verbose or conf['verbose']:
                    print 'os.rename("' + os.path.join(my_pop, _file) + '", "' + standardize(linux_name(os.path.join(my_pop, _file), conf), conf, False) + '")' #debug
                new_filename = standardize(linux_name(os.path.join(my_pop, _file), conf), conf, args.verbose) 
                os.rename(os.path.join(my_pop, _file), new_filename)
            convert(new_filename, conf)
            img_convert(new_filename, conf)
            ps_convert(new_filename, conf)
            if conf['convert_pdf_to_ps'] and conf['convert_ps_to_pdf']:
                print 'both pdf to ps and ps to pdf conversions are selected in conf file.'
        new_name = standardize(linux_name(my_pop, conf), conf, False) 
        if args.verbose or conf['verbose']:
            print 'shutil.move("' + my_pop + '", "' + new_name + '")' #debug
        if os.path.isdir(new_name):
            shutil.rmtree(new_name)
        shutil.move(my_pop, standardize(linux_name(my_pop, conf), conf, args.verbose))
        print 'debug'
