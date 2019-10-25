import matplotlib.projections as     proj
import linestyle.publication              as     LS
import matplotlib.pyplot      as     plt
from MatplotlibTemplate       import *







class CustomTemplate(MatplotlibTemplate):
    """ 

    Customized Projection

    """
    name = 'customtemplate'

    def plot(self, x, y, style = LS.Black[0], **kwargs):
        
        return super().plot(x, y, linewidth = style.linewidth, 
                                  color     = style.color    ,
                                  dashes    = style.dashes   ,  **kwargs)
    




proj.register_projection(CustomTemplate)