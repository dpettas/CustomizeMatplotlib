from my_mpl_template.value import *
import sys 
class Row():

    def __init__(self, columns, vals):
        self.columns = columns.split()
        self.vals    = vals
        self.values  = []
        self.set_values() 

#//////////////////////////////////////////////////////////////////////////////////
#                    BOOLEANS
#//////////////////////////////////////////////////////////////////////////////////

    def vals_are_equal_to_cols  (self  ): return len(self.columns) == len(self.vals) 
    def column_exists           (self,c): return c.strip() in self.get_column_names()
#//////////////////////////////////////////////////////////////////////////////////
#                    GETTERS
#//////////////////////////////////////////////////////////////////////////////////
    def get_number_commits      (self)  : return len(self.columns)   
    def get_column_names        (self)  : return " ".join(self.columns) 
    def get_column_index        (self,c):
        
        if not self.column_exists(c): return -1
        # Scan for finding the value number
        for i,v in enumerate(self.values):
                if v.is_the_name (c): return i

#//////////////////////////////////////////////////////////////////////////////////
#                    SETTERS
#//////////////////////////////////////////////////////////////////////////////////

    def set_values              (self):
        if not self.vals_are_equal_to_cols():
            sys.exit("Error from Row class: not the same number of column with the values")

        for i in range(self.get_number_commits()):
            self.values.append( Value(self.columns[i], self.vals[i] ) )

#//////////////////////////////////////////////////////////////////////////////////
#                    MAGIC METHODS
#//////////////////////////////////////////////////////////////////////////////////
    def __getitem__(self,c):
        idx = self.get_column_index(c)
        return self.values[idx].get_value()

    def __repr__(self):
        out = "Representation of Row (columns) : (value) \n \n"
        for v in self.values:
            out += repr(v) + "\n"

        return out


if __name__ == "__main__":

    v = Row("Re Ka De", [2.0, 10.0 , 5.0])

    print( v["De"] ) 
