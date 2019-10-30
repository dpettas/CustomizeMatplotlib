import matplotlib.projections                      as proj
import my_mpl_template.linestyle.publication       as LS
import matplotlib.pyplot                           as plt
import matplotlib.tri                              as mtri
import numpy                                       as np
from   my_mpl_template.template.matplotlibtemplate import *
from   collections                                 import OrderedDict





class CustomTemplate(MatplotlibTemplate):
    """ 

    Customized Projection

    """
    name = 'customtemplate'

    def plot(self, x, y, style = None, **kwargs):
        
        if style: 
            kwargs["linewidth"] = style.linewidth
            kwargs["color"]     = style.color
            kwargs["dashes"]    = style.dashes
            kwargs["alpha"]     = style.alpha


        return super().plot(x, y, **kwargs)

    def triplot(self, *args, style = None,  **kwargs):
        
        if style: 
            kwargs["linewidth"] = style.linewidth * 0.15
            kwargs["color"]     = style.color
            kwargs["dashes"]    = style.dashes
            kwargs["alpha"]     = style.alpha


        return super().triplot(*args, **kwargs)

    def tricontourf(self, *args, style = None,  **kwargs):
        
        if style: 
            # kwargs["linewidth"] = style.linewidth * 0.15
            # kwargs["c"]     = style.color
            # kwargs["dashes"]    = style.dashes
            kwargs["alpha"]     = style.alpha


        return super().tricontourf(*args, **kwargs)

    def tricontour(self, *args, style = None,  **kwargs):
        
        if style: 
            # kwargs["linewidth"] = style.linewidth * 0.15
            # kwargs["c"]     = style.color
            # kwargs["dashes"]    = style.dashes
            kwargs["alpha"]     = style.alpha


        return super().tricontour(*args, **kwargs)

    def tristreamplot(self, x, y, triangles, Vx, Vy, discretization = 1000, *args, **kwargs):
        
        triang = mtri.Triangulation(x,y,triangles)

        if isinstance(discretization,tuple):

            nx = discretization[0]
            ny = discretization[1]
        else:
            nx = ny = discretization

        xd, yd    = np.meshgrid(
                                np.linspace(x.min() - 0.10, x.max() + 0.10 , nx), 
                                np.linspace(y.min() - 0.10, y.max() + 0.10 , ny)
                               )

        Vx_inter = mtri.LinearTriInterpolator(triang, Vx )
        Vy_inter = mtri.LinearTriInterpolator(triang, Vy )

        Vxd      = Vx_inter(xd, yd)
        Vyd      = Vy_inter(xd, yd)

        # <><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><>

        if 'linewidth' in kwargs and not isinstance(kwargs["linewidth"], float):
          linewidth_inter = mtri.LinearTriInterpolator(triang, kwargs["linewidth"] )
          kwargs["linewidth"] = linewidth_inter(xd, yd)

        if 'color'     in kwargs and not isinstance(kwargs["color"], str):
          color_inter = mtri.LinearTriInterpolator(triang, kwargs["color"] )
          kwargs["color"] = color_inter(xd, yd)

        return super().streamplot(xd, yd, Vxd, Vyd, ** kwargs)

    def background(self, x,y,triangles,val=0.4, **kwargs):
        cmaps = {}
        cmaps['Sequential'] = [
                                'Greys', 'Purples', 'Blues', 'Greens', 'Oranges', 'Reds',
                                'YlOrBr', 'YlOrRd', 'OrRd', 'PuRd', 'RdPu', 'BuPu',
                                'GnBu', 'PuBu', 'YlGnBu', 'PuBuGn', 'BuGn', 'YlGn'
                              ]


        if 'cmap' in kwargs: 
            if not kwargs['cmap'] in cmaps['Sequential']:
                print("The Acceptable cmap for background method are :")
                print(' , '.join(cmaps['Sequential']) )

                cmap = 'Blues'
            else:
                cmap = kwargs['cmap']
        else               : cmap = 'Blues'


        return super().tripcolor(x,y,triangles, [val] * x.size, shading='flat' , cmap   =cmap, vmin   = 0.0   , vmax   = 1.0)


proj.register_projection(CustomTemplate)
