# Map of tuple to id ('name', level(int)) --> id (int)
__paths_map = {}

def anonymize_path(path):
    global __paths_map
    # Anonymize paths consistently leaving top level folders intact
    # e.g. /dev/anon0/anon1
    path_list = path.split('/')
    anon_list = []
    level = 0
    for name in path_list:
        if name == '':
            continue
        # Top level, leave intact
        if path.startswith('/') and level == 0:
            anon_list.append('/' + name)
            level += 1
            continue
        if (name, level) not in __paths_map:
            name_id = len(__paths_map)
            __paths_map[(name, level)] = name_id
        name_id = __paths_map[(name, level)]
        anon_name = 'anon' + str(name_id)
        anon_list.append(anon_name)
    
    anon_path = '/'.join(anon_list)
    if path.endswith('/'):
        anon_path += '/'
    return anon_path


__proc_map = {}

def anonymize_proc(proc_name):
    global __proc_map
    if proc_name not in __proc_map:
        proc_id = len(__proc_map)
        __proc_map[proc_name] = proc_id
    proc_id = __proc_map[proc_name]
    return 'anon_proc' + str(proc_id)