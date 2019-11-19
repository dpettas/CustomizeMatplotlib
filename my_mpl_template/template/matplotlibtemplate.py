
from   matplotlib.axes        import Axes
from   matplotlib             import ticker

__SUBSCRIPTFONTSIZE__ = 18

icounter = -1
subscripts = [r"$(a)$",r"$(b)$",r"$(c)$",r"$(d)$",r"$(e)$",r"$(d)$",r"$(f)$",r"$(g)$",r"$(i)$"]


class MatplotlibTemplate(Axes):
    """ Customized Template """
    name = "matplotlibtemplate"
        
    def set_xlabel  (self, name="", **kwargs):
        return super().set_xlabel(name , rotation = 0.0, **kwargs)        
    def set_ylabel  (self, name="", **kwargs):
        return super().set_ylabel(name , rotation = 0.0, **kwargs)        

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
        if xrange:
            self.set_xlim(left       = xrange[0], 
                          right      = xrange[1],
                          step       = xrange[2],
                          step_minor = xrange[3]  )
        if yrange:
            self.set_ylim(bottom     =  yrange[0],
                          top        =  yrange[1],
                          step       =  yrange[2],
                          step_minor =  yrange[3]  )

    def set_axis_linewidth(self, val, which = 'all'):

        axes = []
        if    which == 'all'   : axes = ['top', 'bottom', 'left', 'right']
        elif  which == 'top'   : axes = ['top'   ]
        elif  which == 'bottom': axes = ['bottom']
        elif  which == 'left'  : axes = ['left'  ]
        elif  which == 'right' : axes = ['right' ]


        for axis in axes: out = self.spines[axis].set_linewidth(val)

        return out




    def xTicksLocator  (self, step = None , step_minor = None):

        if step       : self.xaxis.set_major_locator(ticker.MultipleLocator( step       ))
        if step_minor : self.xaxis.set_minor_locator(ticker.MultipleLocator( step_minor ))

    def yTicksLocator  (self, step = None , step_minor = None):
        
        if step       :self.yaxis.set_major_locator(ticker.MultipleLocator(step       ))
        if step_minor :self.yaxis.set_minor_locator(ticker.MultipleLocator(step_minor ))

    def subscript (self,x = -0.14, y = -0.10, s = None, fontsize = __SUBSCRIPTFONTSIZE__, **kwargs ):

        tmp_s = s
        if not s: tmp_s = self.__get_subscript()

        return super().text( x, y, tmp_s, fontsize = fontsize, fontdict=None,  transform=self.transAxes)


    def __get_subscript(self):
        global icounter
        icounter+= 1
        return subscripts[icounter] 


