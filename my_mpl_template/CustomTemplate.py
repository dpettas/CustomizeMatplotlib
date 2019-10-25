import matplotlib.projections as     proj
import my_mpl_template.linestyle.publication as     LS
from   my_mpl_template.MatplotlibTemplate    import *
import matplotlib.pyplot      as     plt






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
