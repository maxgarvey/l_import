''' /conf.py '''

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

    'convert_pdf_to_ps' : True, #boolean, wether we want to convert pdfs to postscript

    'convert_ps_to_pdf' : False, #boolean, wether we want to convert pdfs to postscript

    'new_file_tree' : {True: {'new_file_tree_prefix' : '_'}},  #Setting this to true will keep the
                                              #original materials as well. prepending the prefix
                                              #specified to the new copy.

    'formats_leave_spaces' : [], #files of these file formats will leave spaces in the names. ex: [".zip",".pdf"]

    'formats_don\'t_touch' : [], #files of these file formats will not be changed at all.     ex: [".zip",".pdf"]

    'verbose': False,
}
