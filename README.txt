l_import
========

an open-source utility for importing files and directories to linux


*** License ***

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


*** Prerequisites ***

Requires python2.7+ to run.
cmd: sudo apt-get install python27

Requires ffmpeg for audio/video conversion.
cmd: sudo apt-get install ffmpeg

Requires ghostscript to convert pdf/ps conversion.
cmd: sudo apt-get install ghostscript

Requires wv to convert from MS Office formats
cmd: sudo apt-get install wv


*** Installation ***

To install, first make sure you have all the prerequisite programs installed.
Then, navigate into the directory: l_import. Then run the lines:

sudo ./install.py

and it will install the files to /usr/bin/ in a usable manner
It is recommended that you change the permissions and ownership
of the file for added security.

sudo cp ./l_import /usr/bin/l_import
cd ..
sudo cp -r l_import /usr/bin/limport
sudo chown <YOUR_UID> /usr/bin/l_import
sudo chown -r <YOUR_UID> /usr/bin/limport

To uninstall, execute the following lines in the console:

sudo rm -f /usr/bin/l_import
sudo rm -rf /usr/bin/limport


*** Usage ***

to use l_import. Enter a shell and type: 

l_import <target dir>

To configure it to your specific needs, use the conf file available in
/usr/bin/limport/conf.py

more on usage of l_import:

usage: l_import [-h] [-o <OUTPUT_LOCATION>] [-v] [-c <CONF_FILE>] <START_POINT>

positional arguments:
  <START_POINT>         the file or directory to convert (recursively).

optional arguments:
  -h, --help            show this help message and exit
  -o <OUTPUT_LOCATION>  the location of the resulting dir/files.
  -v                    toggle_verbosity.
  -c <CONF_FILE>        the location of the conf file you want to use.


*** Configuration ***

The config is located at /usr/bin/limport/conf.py
Edit it and play around with its many options.

The default config follows; to change it, just follow the syntax of
Python dictionaries. For more on that, I'll refer you to diveintopython.org

http://www.diveintopython.net/native_data_types/index.html#odbchelper.dict

Experiment with it to suit your needs:

conf = { 'file_extensions' : 'lowercase', #other options are uppercase or camelcase
    'filenames' : 'lc_underscore',        #lc_underscore, uc_underscore, or camelcase

    'convert_audio' : {True: {'end_format': '.ogg'}},   #boolean is wether we want mp3s converted 
                                                        #or not, the string is the desired end format

    'new_file_tree' : {False: {'new_file_tree_prefix' : '_'}},  #Setting this to true will keep the
                                                                #original materials as well. prepending 
                                                                #the prefix specified to the new copy.

    'formats_leave_spaces' : [], #files of these file formats will leave spaces in the names. ex: [".zip",".pdf"]

    'formats_don\'t_touch' : [], #files of these file formats will not be changed at all.     ex: [".zip",".pdf"]

    'verbose': False,
}
