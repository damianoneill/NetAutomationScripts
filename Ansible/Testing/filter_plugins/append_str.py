class FilterModule(object):

    def append_str(self, l, add_item):
        if type(l) is list:
            for index, item in enumerate(l):
                l[index] = item + add_item
        elif type(l) is dict:
            new_l = {}
            for k, v in l.items():
                new_k = k + add_item
                new_l[new_k] = l[k]
        return new_l

    def filters(self):
        return {'append_str': self.append_str}
