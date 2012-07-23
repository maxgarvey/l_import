import os

def map(start_point):
    if not os.path.isdir(start_point):
        return {}
    else:
        mapping = {}
        order = []
        #print type(start_point) #debug

        for (path, dirs, files) in os.walk(start_point):
            #print str(path)+', '+str(dirs)+', '+str(files) #debug
            mapping[path] = {}
            #mapping[path]['dirs']  = dirs
            mapping[path]['files'] = files
            mapping[path]['depth'] = len(path.split('/'))

        for path in mapping.keys():
            order.append(path)

        order.sort()

        return mapping, order
