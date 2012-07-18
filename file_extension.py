def standardize(name, mode='lower'):
    try:
        name_base = name.split('.')[0]
        name_parts = name.split('.')[1:]
    except:
        return name

    print 'name_base: {}'.format(name_base) #debug
    print 'name_parts: {}'.format(name_parts) #debug

    if mode == 'lower':
        index = 0
        for part in name_parts:
            name_parts[index] = name_parts[index].lower()
            index += 1
        final_name = '.'.join([name_base,('.'.join(name_parts))])
        return final_name

    elif mode == 'upper':
        index = 0
        for part in name_parts:
            name_parts[index] = name_parts[index].upper()
            index += 1
        final_name = '.'.join([name_base,('.'.join(name_parts))])
        return final_name

    elif mode == 'camel':
        index = 0
        for part in name_parts:
            name_parts[index] = name_parts[index].lower()
            name_parts[index] = name_parts[index][0].upper() + name_parts[index][1:]
            index += 1
        final_name = '.'.join([name_base,('.'.join(name_parts))])
        return final_name

    else:
        print 'invalid mode for extension standardization.'
