from .utils import escape_string, unescape_string, first_unescape_string


class DumpsError(Exception):
    pass


class PyStt():
    def dumps(self, data):
        if isinstance(data, dict):
            return '/'.join([self.dumps(k) + '@=' + self.dumps(data[k]) for k in data]) + '/'
        elif isinstance(data, list):
            return '/'.join([self.dumps(i) for i in data]) + '/'
        elif isinstance(data, str):
            return escape_string(data)
        else:
            raise DumpsError('found {}'.format(data))

    def loads(self, data):
        if data.find('/') > 0:
            datas = data.split('/')
            l = []
            #ll = []
            d = {}
            for i in datas:
                if i == '':
                    continue
                if i.find('@A=') > 0:
                    pass
                i_decode = self.loads(i)
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
            if v.find('@AS@S') > 0:
                vs = v.split('@AS@S')
                ll = []
                for it in vs:
                    if it == '':
                        continue
                    it = first_unescape_string(self.loads(it))
                    vvv = self.loads(it)
                    ll.append(vvv)
                return {self.loads(k): ll}
            elif v.find('@A=') > 0:
                vs = v.split('@S')
                dl = {}
                for it in vs:
                    it = first_unescape_string(it)
                    if it == '':
                        continue
                    vvv = self.loads(it)
                    dl.update(vvv)
                return {self.loads(k): dl}
            else:
                if self.loads(v).find('@A=') > 0:
                    vv = self.loads(self.loads(v))
                    return {self.loads(k): vv}
                else:
                    return {self.loads(k): self.loads(v)}
        else:
            return unescape_string(data)
