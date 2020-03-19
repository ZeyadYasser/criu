from .anon_utils import anonymize_path

def reg_handler(entry):
    path = entry['name']
    entry['name'] = anonymize_path(path)
    return entry

def inet_sk_entry(entry):
    return entry

file_entry_handlers = {
    'REG': reg_handler,
    'INETSK': inet_sk_entry,
}

def files_anon_handler(image_dict):
    anon_entries = []
    for entry in image_dict['entries']:
        handler = file_entry_handlers[entry['type']]
        anon_entries.append(handler(entry))
    image_dict['entries'] = anon_entries
    return image_dict