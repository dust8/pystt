def escape_string(s):
    s = s.replace("@", "@A")
    s = s.replace('/', '@S')
    return s


def unescape_string(s):
    s = s.replace("@A", "@")
    s = s.replace('@S', '/')
    return s
