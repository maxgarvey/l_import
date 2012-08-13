'''/map_dirs.py'''
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
