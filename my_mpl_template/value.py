

class Value():

    def __init__(self, name, val):
        self.name = name 
        self.val  = val


    def get_value  (self)  : return self.val
    def get_name   (self)  : return self.name

    def is_the_name(self,c): return c.strip() == self.name

    def __str__    (self)  : return "{} : {}".format(self.name, self.val)
    def __repr__   (self)  : return self.__str__()
