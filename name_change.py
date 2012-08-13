'''/name_change.py'''
from map_dirs import _map
from new_name import linux_name
from file_extension import standardize
from av_conv import convert
from pdf_conv import ps_convert
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
            ps_convert(new_filename, conf)
        new_name = standardize(linux_name(my_pop, conf), conf, False) 
        if args.verbose or conf['verbose']:
            print 'shutil.move("' + my_pop + '", "' + new_name + '")' #debug
        if os.path.isdir(new_name):
            shutil.rmtree(new_name)
        shutil.move(my_pop, standardize(linux_name(my_pop, conf), conf, args.verbose))
        print 'debug'
