from value import *
import sys 
class Row():

    def __init__(self, columns, vals):
        self.columns = columns.split()
        self.vals    = vals
        self.values  = []
        self.set_values() 

#//////////////////////////////////////////////////////////////////////////////////
    def __vals_are_equal_to_cols(self): return len(self.columns) == len(self.vals) 
    def get_number_columns      (self): return len(self.columns)
    def set_values              (self):
        if not self.__vals_are_equal_to_cols():
            sys.exit("Error: not the same number of column with the values")

        for i in range(self.get_number_columns()):
            self.values.append( Value(self.columns[i], self.values[i] ) )








if __name__ == "__main__":

    v = Value("Re", 0.1)
    print(v)

