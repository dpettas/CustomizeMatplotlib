
from   matplotlib.axes        import Axes
from   matplotlib             import ticker
import matplotlib.pyplot      as plt


__SUBSCRIPTFONTSIZE__ = 18


def set_subscriptFontsize(fontsize):

    global __SUBSCRIPTFONTSIZE__
    __SUBSCRIPTFONTSIZE__ = fontsize



icounter = -1
subscripts = [r"$(a)$",r"$(b)$",r"$(c)$",r"$(d)$",r"$(e)$",r"$(d)$",r"$(f)$",r"$(g)$",r"$(i)$"]


class MatplotlibTemplate(Axes):
    """ Customized Template """
    name = "matplotlibtemplate"
    def __init__(self, fig, rect,
                 facecolor= None,  # defaults to rc axes.facecolor
                 frameon  = True,
                 sharex   = None,  # use Axes instance's xaxis info
                 sharey   = None,  # use Axes instance's yaxis info
                 label    = '',
                 xscale   = None,
                 yscale   = None,
                 **kwargs):

        
        Axes.__init__  (self, fig, rect,
                        facecolor= None,  # defaults to rc axes.facecolor
                        frameon  = True,
                        sharex   = None,  # use Axes instance's xaxis info
                        sharey   = None,  # use Axes instance's yaxis info
                        label    = '',
                        xscale   = None,
                        yscale   = None,
                        **kwargs)

        self.x_labelFontSize   = None
        self.y_labelFontSize   = None
        self.legendFontSize    = None
        self.subscriptFontSize = None
        self.textFontsize      = None 

    def increase(self, which = 'all', portion = 1.0):

        self.x_labelsize = plt.rcParams["axes.labelsize"] * portion


        return


    def enlarge(self):
        """
            Note this method should be called before the set_xlabel() and
            set_ylabel().

            A simple function that used with no arguments to standardize
            the linewidth axes width in cases where the subplot occupies 
            a [2,2] space in gridspec.
        """

        major_tick_len         = 15
        major_tick_wid         =  4
        minor_tick_len         =  7
        minor_tick_wid         =  4
        
        axisLinewidth          = 5.5

        x_labelsize            = 32
        x_pad                  = 10 
    
        y_labelsize            = 32
        y_pad                  = 10 
 
        self.x_labelFontSize   = 32
        self.y_labelFontSize   = 32
        self.legendFontSize    = 28

        self.subscriptFontSize = 32
        self.textFontsize      = 32

        out = self.tick_params(which = 'major', length    = major_tick_len,
                                                width     = major_tick_wid)

        out = self.tick_params(which = 'minor', length    = minor_tick_len,
                                                width     = minor_tick_wid)

        out = self.tick_params(axis  = "x"    , labelsize = x_labelsize,
                                                pad       = x_pad)

        out = self.tick_params(axis  = "y"    , labelsize = y_labelsize,
                                                pad       = y_pad)

        self.set_axis_linewidth(axisLinewidth)

        return out



    def set_xlabel  (self, name="", **kwargs):
        """
            this method override the method set_xlabel. 
            Milestones:
            the rotation argument is rotation = 0 to be readable the plot.
            The second milestone is connected with the self.enlarge() method. 
            If the latter method is called then the fontsize of the x_label 
            changes.
        """
        if not "rotation" in kwargs: kwargs["rotation"] = 0.0


        if self.x_labelFontSize and not "fontsize" in kwargs:
            kwargs["fontsize"] = self.x_labelFontSize
       

        return super().set_xlabel(name , **kwargs)        



    def set_ylabel  (self, name="", **kwargs):
        """
            this method override the method set_ylabel. 
            Milestones:
            the rotation argument is rotation = 0 to be readable the plot.
            The second milestone is connected with the self.enlarge() method. 
            If the latter method is called then the fontsize of the y_label 
            changes.
        """

        if not "rotation" in kwargs: kwargs["rotation"] = 0.0


        if self.y_labelFontSize and not "fontsize" in kwargs:
            kwargs["fontsize"] = self.y_labelFontSize
       

        return super().set_ylabel(name , **kwargs)        

       

    def legend(self,*args, **kwargs):
        """
            this method overrides the legend method to incorporate the
            enlarge method of the class
        """


        if self.legendFontSize and not "fontsize" is kwargs:

            kwargs["fontsize"] = self.legendFontSize


        return super().legend(*args, **kwargs)

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
        """
        set_axis_linewidth: 
        Arguments:
        ** val (float) is the linewidth of the axes.
        ** which       define which axes default 'all'
                       possible values 'top', 'bottom', 
                                      'left', 'right'
        """


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


    def text(self, x, y, s, **kwargs):

        if self.textFontsize:
            kwargs["fontsize"] = self.textFontsize


        return super().text(x,y,s, **kwargs)


    def subscript (self,x = -0.14, y = -0.10, s = None, **kwargs ):

        tmp_s = s
        if not s: tmp_s = self.__get_subscript()


        if  not self.subscriptFontSize  and not "fontsize" in kwargs:
            kwargs["fontsize"] = __SUBSCRIPTFONTSIZE__
        elif    self.subscriptFontSize  and not "fontsize" in kwargs: 
            kwargs["fontsize"] = self.subscriptFontSize



        return super().text( x, y, tmp_s,
                            fontsize  = kwargs["fontsize"],
                            fontdict  = None    ,
                            transform =self.transAxes)


    def __get_subscript(self):
        global icounter
        icounter+= 1
        return subscripts[icounter] 

    def ticksRename(self, xticks = None, yticks = None):
        """
        This method renames the ticks of the x and y axis. 
        as arguments we use the x_ticks and y_ticks.
        These values by default are None. 
        In general the latter values must be lists.
        """
        out_x = None 
        out_y = None

        bool_x = isinstance(xticks,list)
        bool_y = isinstance(yticks,list)

        if bool_x: out_x = self.set_xticklabels(xticks)
        if bool_y: out_y = self.axes.get_yaxis().set_ticks(yticks)

        return out_x, out_y

    def ticksNull(self, which = 'both'):
        """
        Removes the tick labels from the x or y axis. 
        Optional argument which = "both" or "x" or "y"

        """

        if   which == 'both': return self.ticksRename(xticks = []  , yticks = []  )
        elif which == 'x'   : return self.ticksRename(xticks = []  , yticks = None)
        elif which == 'y'   : return self.ticksRename(xticks = None, yticks = []  )


        
    def xticksNull(self): return self.ticksRename(xticks = []  , yticks = None)
    def yticksNull(self): return self.ticksRename(xticks = None, yticks = []  )


