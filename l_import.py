from conf import *
from file_extension import *
from map_dirs import *
from name_change import *
from new_name import *
from argparse import ArgumentParser

#print dir() #debug

if __name__ == "__main__":
    #the main method

    #create a new parser object
    parse = ArgumentParser()
    #mandatory, possibly multiple positional arguments for directories to look ito
    parse.add_argument('location', nargs='+', help='enter paths which you would like to recursively')
    args = parse.parse_args()

    print args.location #debug
