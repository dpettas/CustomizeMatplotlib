import matplotlib.projections                      as     proj
import my_mpl_template.linestyle.publication       as     LS
import matplotlib.pyplot                           as     plt
from   my_mpl_template.template.matplotlibtemplate import *






class CustomTemplate(MatplotlibTemplate):
    """ 

    Customized Projection

    """
    name = 'customtemplate'

    def plot(self, x, y, style = None, **kwargs):
        
        if style:
          kwargs['linewidth'] = style.linewidth
          kwargs['color']     = style.color
          kwargs['dashes']    = style.dashes


        return super().plot(x, y, **kwargs)
    



    def triplot(self,*args, style = None, **kwargs):

      if style:
        kwargs['linewidth'] = style.linewidth * 0.15
        kwargs['color'    ] = style.color
        kwargs['dashes'   ] = style.dashes
        kwargs['alpha'    ] = style.alpha

      
      return super().triplot(*args, **kwargs)
    

proj.register_projection(CustomTemplate)
