'''/name_change.py'''
from map_dirs import _map
from new_name import linux_name
from file_extension import standardize
import os

def change_names(start_point):
    '''this method will take a starting point and change all
    the names to more linux friendly ones'''
    dir_map, ordering = _map(start_point)
    while len(ordering) > 0:
        my_pop = ordering.pop()
        print '\npopped: ' + my_pop #debug
        print 'dir_map["' + my_pop + '"]["files"]: ' + str(dir_map[my_pop]["files"]) #debug
        for _file in dir_map[my_pop]["files"]:
            print 'os.rename("' + os.path.join(my_pop, _file) + '", "' + standardize(linux_name(os.path.join(my_pop, _file))) + '")' #debug
        print 'os.rename("' + my_pop + '", "' + standardize(linux_name(my_pop)) + '")' #debug
        #os.rename(linux_name(my_pop))
