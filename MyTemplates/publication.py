import matplotlib.projections as     proj
import numpy                  as     np
import LineStyle              as     LS
import matplotlib.ticker      as     ticker
import matplotlib.pyplot      as     plt
from   matplotlib.axes        import Axes



plt.rcParams.update({'text.usetex'         : True  } )
plt.rcParams.update({'text.latex.preamble' :r'\usepackage{nicefrac}'})

plt.rcParams.update({'axes.linewidth'      :  3.0  } )
plt.rcParams.update({'axes.labelsize'      : 18.0  } )
plt.rcParams.update({'font.size'           : 16.0  } )
plt.rcParams.update({'font.weight'         :'bold' } )

plt.rcParams.update({'xtick.top'           : True })
plt.rcParams.update({'xtick.bottom'        : True })
plt.rcParams.update({'xtick.major.size'    : 8.0  })
plt.rcParams.update({'xtick.minor.size'    : 4.0  })
plt.rcParams.update({'xtick.major.width'   : 2.5  })
plt.rcParams.update({'xtick.minor.width'   : 2.5  })
plt.rcParams.update({'xtick.direction'     : 'in' })
plt.rcParams.update({'xtick.minor.visible' : True })
plt.rcParams.update({'xtick.major.pad'     : 3    })

plt.rcParams.update({'ytick.left'          : True })
plt.rcParams.update({'ytick.right'         : True })
plt.rcParams.update({'ytick.major.size'    : 8.0  })
plt.rcParams.update({'ytick.minor.size'    : 4.0  })
plt.rcParams.update({'ytick.major.width'   : 2.5  })
plt.rcParams.update({'ytick.minor.width'   : 2.5  })
plt.rcParams.update({'ytick.direction'     : 'in' })
plt.rcParams.update({'ytick.minor.visible' : True })

plt.rcParams.update({'legend.frameon'      : False})
plt.rcParams.update({'legend.fontsize'     : 16   })




__SUBSCRIPTFONTSIZE__ = 21


subscripts = [r"$(a)$", r"$(b)$", r"$(c)$", r"$(d)$", r"$(e)$", r"$(f)$"]
icounter   = -1  


class MatplotlibTemplate(Axes):
    """ Template """
    name = "matplotlibtemplate"
        
    def set_xlabel  (self, name="", **kwargs): return super().set_xlabel(name , rotation = 0.0, **kwargs)        
    def set_ylabel  (self, name="", **kwargs): return super().set_ylabel(name , rotation = 0.0, **kwargs)        

    def set_xlim (self, left=None, right=None, step=None, step_minor=None, *args, **kwargs):

        self.xTicksLocator(step       = step      )
        self.xTicksLocator(step_minor = step_minor)
        self.xaxis.set_label_coords( 0.500,-0.075)
        return super().set_xlim(left, right)

    def set_ylim (self, bottom=None, top=None, step=None, step_minor=None, *args, **kwargs):
                        
        self.yTicksLocator(step       = step      )
        self.yTicksLocator(step_minor = step_minor)
        self.yaxis.set_label_coords(-0.110, 0.500)
        return super().set_ylim(bottom, top)

    def set_limit(self, xrange = None, yrange = None):

        self.set_xlim(left    = xrange[0], right =  xrange[1], step = xrange[2], step_minor = xrange[3]  )
        self.set_ylim(bottom  = yrange[0], top   =  yrange[1], step = yrange[2], step_minor = yrange[3]  )

    def xTicksLocator  (self, step = None , step_minor = None):

        if step       : self.xaxis.set_major_locator(ticker.MultipleLocator( step       ))
        if step_minor : self.xaxis.set_minor_locator(ticker.MultipleLocator( step_minor ))

    def yTicksLocator  (self, step = None , step_minor = None):
        
        if step       :self.yaxis.set_major_locator(ticker.MultipleLocator(step       ))
        if step_minor :self.yaxis.set_minor_locator(ticker.MultipleLocator(step_minor ))

    def subscript (self,x = -0.14, y = -0.10, s = None, fontsize = __SUBSCRIPTFONTSIZE__, **kwargs ):

        tmp_s = s
        if not s: tmp_s = self.__get_subscript()

        return super().text( x, y, tmp_s, fontsize = fontsize, fontdict=None, withdash=False, transform=self.transAxes)


    def __get_subscript(self):
        global icounter
        icounter+= 1
        return subscripts[icounter] 




class Publication(MatplotlibTemplate):
    """ 

    Customized Projection

    """
    name = 'publication'

    def plot(self, x, y, style = LS.Black[0], **kwargs):
        
        return super().plot(x, y, linewidth = style.linewidth, 
                                  color     = style.color    ,
                                  dashes    = style.dashes   ,  **kwargs)
    




proj.register_projection(Publication)
