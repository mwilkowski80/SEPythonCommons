
class Optional(object):
    def __init__(self, obj):
        self.obj = obj

    def map(self, map_func):
        if self.obj:
            return Optional(map_func(self.obj))
        else:
            return self

    def or_else(self, else_obj):
        return self.obj or else_obj

    def or_else_supplier(self, else_obj_supplier):
        return self.obj or else_obj_supplier()
