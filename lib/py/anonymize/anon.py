from .files_anon_handler import files_anon_handler 
from .core_anon_handler import core_anon_handler 

anon_handlers = {
    'CORE': core_anon_handler,
    'FILES': files_anon_handler,
}

def anonymize_image(image_dict):
    magic = image_dict['magic']
    if magic not in anon_handlers:
        print("Anonymization for %s is not supported" % magic)
        return

    handler = anon_handlers[magic]
    return handler(image_dict)
