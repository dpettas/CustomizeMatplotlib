import matplotlib.projections                      as proj
import my_mpl_template.linestyle.publication       as LS
import matplotlib.pyplot                           as plt
import matplotlib.tri                              as mtri
import matplotlib                                  as mpl
import numpy                                       as np
from   my_mpl_template.template.matplotlibtemplate import *
from   collections                                 import OrderedDict
from matplotlib.markers                            import MarkerStyle





class CustomTemplate(MatplotlibTemplate):
    """ 

    Customized Projection

    """
    name = 'customtemplate'

    def plot(self, x, y, mkr = None, style = None, **kwargs):
        
        if style: 
            kwargs["linewidth"] = style.linewidth
            kwargs["color"]     = style.color
            kwargs["dashes"]    = style.dashes
            kwargs["alpha"]     = style.alpha

        if not mkr: mkr = '-'

        return super().plot(x, y, mkr, **kwargs)

    def verticalline(self, val, mkr = None, style = None, ylim = None, **kwargs):


        xlim  = self.get_xlim()
        _ylim = self.get_ylim()

        if ylim: _ylim = ylim


        x = [ val ] * 2
        y = _ylim
        return self.plot(x,y,mkr,style,**kwargs)


    def triplot(self, *args, style = None,  **kwargs):
        
        if style: 
            kwargs["linewidth"] = style.linewidth * 0.15
            kwargs["color"]     = style.color
            kwargs["dashes"]    = style.dashes
            kwargs["alpha"]     = style.alpha


        return super().triplot(*args, **kwargs)

    def tricontourf(self, *args, style = None,  **kwargs):
        
        # if style: 
            # # kwargs["linewidth"] = style.linewidth * 0.15
            # # kwargs["c"]         = style.color
            # # kwargs["dashes"]    = style.dashes
            # kwargs["alpha"]       = style.alpha


        return super().tricontourf(*args, **kwargs)

    def tricontour(self, *args, style = None,  **kwargs):
        
        if style: 
            # kwargs["linewidth"] = style.linewidth
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
                                'Greys' , 'Purples', 'Blues' , 'Greens', 'Oranges', 'Reds',
                                'YlOrBr', 'YlOrRd' , 'OrRd'  , 'PuRd'  , 'RdPu'   , 'BuPu',
                                'GnBu'  , 'PuBu'   , 'YlGnBu', 'PuBuGn', 'BuGn'   , 'YlGn'
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




    def markerpoint(self,x,y,mkr='o',fillstyle = 'full', s = 100, 
                    edgecolors = LS.Black[0].getColor(),
                    linewidth  = 2                     ,
                    facecolors = LS.White[0].getColor(), 
                    zorder=100, label = None ):


        super().scatter(x,y, marker = mkr,s = s, edgecolors = edgecolors    , 
                                                 linewidth  = linewidth     ,
                                                 facecolors = facecolors    ,
                                                 zorder = zorder, label=label)

        if not fillstyle == 'none':
            _marker = MarkerStyle(mkr,fillstyle)
            super().scatter(x,y, marker = _marker, s= s, edgecolors = edgecolors, 
                                                         linewidth  = linewidth ,
                                                         facecolors = edgecolors,
                                                         zorder     = zorder + 1)
        



    def createcolorbar(self,vmin, vmax,levels = 10, ticks = None, cmap = mpl.cm.RdBu_r, orientation = "vertical"):
        """
            createcolorbar is a method to plot colorbar in a subplot.
            ** vmin     low value of the bar 
            ** vmax   upper value of the bar
            ** levels number of levels in the colormap 
            ** ticks (default None) if value ticks is None then the 

                ticks = np.linpace(vmin,vmax, levels)
                else ticks may be a list which contains the custom value like
                ticks = [-10,-5, 0, 5, 10]

            ** cmap is the specific choice for the color bar by default is
                (mpl.cm.RdBu_r)
            ** orientation is the oriantation of the colorbar (default vertical)

        """
        bounds = np.linspace         (vmin,vmax, levels)
        norm   = mpl.colors.Normalize(vmin,vmax)

        if not ticks: ticks = bounds

        cb3 = mpl.colorbar.ColorbarBase(self, cmap      = cmap,
                                              norm      = norm,
                                              boundaries= bounds,
                                              extend    = 'both',
                                              extendfrac= 'auto',
                                              ticks     =  ticks,
                                              # spacing   = 'uniform',
                                              orientation=orientation)
        cb3.minorticks_off()
        cb3.ax.tick_params(labelsize=22,direction = 'out', length = 4) 
        super().set_aspect(20.0)

        return cb3




proj.register_projection(CustomTemplate)
