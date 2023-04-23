def find_value(obj, value=None, path=None, all_paths=[], key= lambda a,b: a==b, first_match=True):
    if path is None:
        path = []
        all_paths = []
    for k, v in iter_object(obj):
        if key(v, value):
            all_paths.append(path + [k])
            if first_match:
                break
        elif k is None:
            continue
        else:
            all_paths = find_value(v, value, path + [k], all_paths, key, first_match)
            if first_match and all_paths:
                break
    return all_paths

"""
def get_json_path(obj, value=None, path=None):
    if path is None:
        path = []
    for k, v in iter_object(obj):
        if v == value:
            return path + [k] 
        elif k is None:
            continue
        else:
            path.append(k)
            result = get_json_path(v, value=value, path=path)
            if result: 
                return result
            path.pop()
"""


def iter_object(obj):
    if isinstance(obj, list):
        for k, item in enumerate(obj):
            yield k, item
    elif isinstance(obj, dict):
        for k, item in obj.items():
            yield k, item
    else:
        yield None, obj
