''' /conf.py '''

'''this dict will serve as a conf file for l_import'''
conf = {
    'file_extensions' : 'lowercase' #other options are uppercase or camelcase
    'filenames' : 'lc_underscores'  #lc_underscore, uc_underscore, or camelcase
    'convert_mp3' : {True, 'format': 'ogg'}   #boolean is wether we want mp3s converted or not,
                                              #the string is the desired end format
    'new_file_tree' : {False, 'new_files_prefix' : '_'}  #Setting this to true will keep the
                                              #original materials as well. prepending the prefix
                                              #specified to the new copy.
    
}
