from .utils import escape_string, unescape_string


class DumpsError(Exception):
    pass


def dumps(data):
    if isinstance(data, dict):
        return '/'.join([dumps(k) + '@=' + dumps(data[k]) for k in data])
    elif isinstance(data, list):
        return '/'.join([dumps(i) for i in data])
    elif isinstance(data, str):
        return escape_string(data)
    else:
        raise DumpsError('expected {}'.format(data))


def loads(data):
    if data.find('/') > 0:
        datas = data.split('/')
        l = []
        d = {}
        for i in datas:
            i_decode = loads(i)
            if isinstance(i_decode, dict):
                d.update(i_decode)
            else:
                l.append(i_decode)
        if d == {}:
            return l
        else:
            return d
    elif data.find('@=') > 0:
        k, v = data.split('@=')
        return {loads(k): loads(v)}
    else:
        return unescape_string(data)
