class FilterModule(object):

    def append_str(self, l, add_item):
        for index, item in enumerate(l):
            l[index] = item + add_item
        return l

    def filters(self):
        return {'append_str': self.append_str}
