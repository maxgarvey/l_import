'''/new_name.py'''

def linux_name(existing_filename, mode='lc_underscore'):
    '''this method will take an existing filename and return the
    linuxized filename camelcase or underscored'''

    l_filename = ''

    #camelcase
    if mode == 'camelcase':
        l_filename = existing_filename.replace('\\ ','_').replace(' ','_')
    else:
        position = 0
        positions = []
        not_done = True

        while not_done:
            try:
                position = existing_filename.index('\ ')
                existing_filename = existing_filename[:position] + \
                    existing_filename[(position+2):(position+3)].upper() + \
                    existing_filename[(position+3):]
            except ValueError, err:
                not_done = False

        not_done = True
        while not_done:
            try:
                position = existing_filename.index(' ')
                existing_filename = existing_filename[:position] + \
                    existing_filename[(position+1):(position+2)].upper() + \
                    existing_filename[(position+2):]
            except ValueError, err:
                not_done = False

        l_filename = existing_filename

    #lowercase with underscores
    if mode == 'lc_underscore':
        try:
            l_filename = l_filename[:l_filename.rindex('.')].lower() + l_filename[l_filename.rindex('.'):]
        except Exception, err:
            l_filename = l_filename.lower()

    #uppercase with underscores
    if mode == 'uc_underscore':
        try:
            l_filename = l_filename[:l_filename.rindex('.')].upper() + l_filename[l_filename.rindex('.'):]
        except Exception, err:
            l_filename = l_filename.upper()
       

    return l_filename
