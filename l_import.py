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

    if args.verbose or conf['verbose']:
        print 'args:{0}\nconf{1}'.format(args, conf)

    change_names(args, conf)
    

