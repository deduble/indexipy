def find_value(obj, value=None, path=None, all_paths=[], key= lambda a,b: a==b, first_match=True):
    if path is None:
        path = []
        all_paths = []
    for k, v in iter_object(obj):
        if key(v, value):
            all_paths.append( (path + [k]) )
            if first_match:
                break
        elif k is None:
            continue
        else:
            all_paths = find_value(v, value, path + [k], all_paths, key, first_match)
            if first_match and all_paths:
                break
    return Index(all_paths)

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


class Index:
    def __init__(self, *args):
        self.indices = args[0]

    def __getitem__(self, container):
        if isinstance(container, dict):
            return [container[key] for key in self.indices]
        else:
            return [container[index] for index in self.indices]
    
    def __repr__(self):
        return str(f'Index({self.indices[:20]}...)')
    
    def __str__(self):
        return str(self.indices)


class array:
    def __init__(self, data):
        self.data = data

    def __getitem__(self, key):
        if isinstance(key, tuple):
            return self._advanced_indexing(key)
        else:
            return self.data[key]

    def __setitem__(self, key, value):
        if isinstance(key, tuple):
            self._advanced_indexing(key, value=value)
        else:
            self.data[key] = value

    def _advanced_indexing(self, key, value=None):
        if len(key) == 1:
            return self.__getitem__(key[0]) if value is None else self.__setitem__(key[0], value)
        else:
            idx = key[0]
            if isinstance(idx, slice):
                indices = list(range(*idx.indices(len(self.data))))
            elif isinstance(idx, list) or isinstance(idx, np.ndarray):
                indices = idx
            else:
                indices = [idx]

            # Recursively call _advanced_indexing
            return [self._advanced_indexing(key[1:], value=value) for idx in indices]
