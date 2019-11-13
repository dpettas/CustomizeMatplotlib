
import matplotlib.pyplot                           as     plt
from   matplotlib.figure                           import Figure
from   my_mpl_template.template.customtemplate     import *

__X_FIGSIZE_INCHES__ = 6.4
__Y_FIGSIZE_INCHES__ = 4.8


class ConstFigSize(Figure):
    def __init__(self, nrows = 1, ncols = 1,figsize= (__X_FIGSIZE_INCHES__,__Y_FIGSIZE_INCHES__),totalfigsize=None,  *args, **kwargs):
        """
        	
        	custom kwarg figtitle is a figure title

        """
        if not totalfigsize:
            _figsize = (figsize[0] * ncols, figsize[1] * nrows)
        else: 
            _figsize = totalfigsize

        super().__init__(_figsize, *args, **kwargs)
        

    def add_subplot(self, gridspec, **kwargs ):

        return super().add_subplot( gridspec, **kwargs, projection = 'customtemplate'   )




def figure(nrows = 1, ncols =1, figsize= (__X_FIGSIZE_INCHES__,__Y_FIGSIZE_INCHES__),totalfigsize=None, **gskwargs):


	fig = plt.figure(FigureClass= ConstFigSize, nrows = nrows, ncols = ncols, figsize = figsize, totalfigsize = totalfigsize)
	gs  = fig.add_gridspec(nrows, ncols, **gskwargs)

	return fig, gs


