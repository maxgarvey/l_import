#!/usr/bin/python

import shutil
import os

shutil.copy('./l_import', '/usr/bin/l_import')
shutil.copytree('../l_import', '/usr/bin/limport')

os.chmod('/usr/bin/l_import', 0777)
os.chmod('/usr/bin/limport', 0777)
