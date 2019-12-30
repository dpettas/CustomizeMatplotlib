import numpy as np
import sys 


class Column():
    """
	
    """
    def __init__(self, name, data):

        if not isinstance(data, np.ndarray): 
            sys.exit('[Error]: data in Column should be np.ndarray')

        self.name = name 
        self.data = data


		
