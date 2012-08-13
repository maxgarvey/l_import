''' /conf.py '''

'''this dict will serve as a conf file for l_import'''
conf = {
    'file_extensions' : 'lowercase', #other options are uppercase or camelcase

    'filenames' : 'lc_underscore',  #lc_underscore, uc_underscore, or camelcase

    'convert_audio' : {True: {'end_format': '.ogg'}},   #boolean, whether we want audio files converted or not,
                                                    #the string is the desired end format

    'convert_img' : {True: {'end_format': '.png'}},   #boolean, whether we want img files converted or not,
                                                      #the string is the desired end format

    'convert_word' : {True: {'end_format' : '.odt'}}, #boolean, whether we want Word files (or Word-like
                                                      #programs' files) converted. Inner dict has desired
                                                      #end format.

    'convert_pdf_to_ps' : True #boolean, wether we want to convert pdfs to postscript

    'convert_ps_to_pdf' : False #boolean, wether we want to convert pdfs to postscript

    'new_file_tree' : {False: {'new_file_tree_prefix' : '_'}},  #Setting this to true will keep the
                                              #original materials as well. prepending the prefix
                                              #specified to the new copy.

    'formats_leave_spaces' : [], #files of these file formats will leave spaces in the names. ex: [".zip",".pdf"]

    'formats_don\'t_touch' : [], #files of these file formats will not be changed at all.     ex: [".zip",".pdf"]

    'verbose': False,
}
