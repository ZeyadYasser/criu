from .anon_utils import anonymize_proc

def x86_64_handler(core_entry):
    # TODO: erase register values
    return core_entry

def arm_handler(core_entry):
    # TODO: erase register values
    return core_entry

arch_core_entry_handlers = {
    'X86_64': x86_64_handler,
    'ARM': arm_handler,
}


def core_anon_handler(image_dict):
    # image_dict['entries'] contains a single entry
    core_entry = image_dict['entries'][0]
    # anonymize process name
    if 'tc' in core_entry:
        proc_name = core_entry['tc']['comm']
        core_entry['tc']['comm'] = anonymize_proc(proc_name)
    if 'thread_core' in core_entry and \
       'comm' in core_entry['thread_core']:
       proc_name = core_entry['thread_core']['comm']
       core_entry['thread_core']['comm'] = anonymize_proc(proc_name)
    # TODO: anoymize creds
    # arch-dependant anonymization
    mtype = core_entry['mtype']
    handler = arch_core_entry_handlers[mtype]
    image_dict['entries'][0] = handler(core_entry)
    return image_dict
