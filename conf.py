''' /conf.py '''

'''this dict will serve as a conf file for l_import'''
conf = {
    'file_extensions' : 'lowercase', #other options are uppercase or camelcase
    'filenames' : 'lc_underscores',  #lc_underscore, uc_underscore, or camelcase
    'convert_audio' : {True: {'end_format': 'ogg'}},   #boolean is wether we want mp3s converted or not,
                                                    #the string is the desired end format
    'new_file_tree' : {False: {'new_files_prefix' : '_'}},  #Setting this to true will keep the
                                              #original materials as well. prepending the prefix
                                              #specified to the new copy.
    'formats_leave_spaces' : [], #files of these file formats will leave spaces in the names
    'formats_don\'t_touch' : [], #files of these file formats will not be changed at all
}
