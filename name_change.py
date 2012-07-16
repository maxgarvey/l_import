def linux_name(existing_filename, camel_case=False):
    '''this method will take an existing filename and return the
    linuxized filename camelcase or underscored'''
    l_filename = ''
    if not camel_case:
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

    return l_filename
