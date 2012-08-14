''' /pdf_conv.py '''

from subprocess import call
import os

def ps_convert(filename, conf):
    '''this method will convert the file from pdf to ps or vice versa'''

    extension = os.path.splitext(filename)[1].lower()
    if extension == '.pdf':
        if conf['convert_pdf_to_ps'] and not conf['convert_ps_to_pdf']:
            if conf['verbose']:
                print "pdf2ps {}".format(filename)
            call(['pdf2ps', filename])

    elif extension == '.ps':
        if conf['convert_ps_to_pdf'] and not conf['convert_pdf_to_ps']:
            if conf['verbose']:
                print "ps2pdf {}".format(filename)
            call(['ps2pdf', filename])
