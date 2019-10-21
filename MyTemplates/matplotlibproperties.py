from   matplotlib.axes        import Axes
from   matplotlib.gridspec    import GridSpec
import matplotlib.pyplot      as     plt
import matplotlib.projections as     proj
import matplotlib.ticker      as     ticker
import numpy                  as     np


from FileData   import FileData
from LineStyle  import *        




__STEP__              =  2.0
__STEP_MINOR__        =  0.5
__AXISLINEWIDTH__     =  2.0
__AXISFONTSIZE__      = 18.0
__MAJORTICKS_LENGTH__ =  8.0
__MAJORTICKS_WIDTH__  =  2.3
__MINORTICKS_LENGTH__ =  4.0
__MINORTICKS_WIDTH__  =  2.3



def PlottingMode( mode = "Normal"):
    """

        mode : Normal or Presentation

    """

    global __STEP__             , __AXISLINEWIDTH__   , __AXISFONTSIZE__, \
           __MAJORTICKS_LENGTH__, __MAJORTICKS_WIDTH__, \
           __MINORTICKS_LENGTH__, __MINORTICKS_WIDTH__, __STEP_MINOR__

    if mode.lower() == "normal":
        __STEP__              = 5.0
        __AXISLINEWIDTH__     = 2.0
        __AXISFONTSIZE__      = 18.0
        __MAJORTICKS_LENGTH__ = 8
        __MAJORTICKS_WIDTH__  = 2.3
        __MINORTICKS_LENGTH__ = 4
        __MINORTICKS_WIDTH__  = 2.3
    elif mode.lower() == "presentation":
        __STEP__              = 10.0
        __AXISLINEWIDTH__     = 2.0
        __AXISFONTSIZE__      = 18.0
        __MAJORTICKS_LENGTH__ = 8
        __MAJORTICKS_WIDTH__  = 2.3
        __MINORTICKS_LENGTH__ = 4
        __MINORTICKS_WIDTH__  = 2.3




PlottingMode( mode = "Normal")




class MyTemplate(Axes):
    """ 

    Customized Projection

    """
    name = 'MyTemplate'

    plt.rcParams['text.latex.preamble']= [r'\usepackage{nicefrac}']

    plt.rcParams.update({'text.usetex'   : True } )
    plt.rcParams.update({'font.size'     : 15   } )
    plt.rcParams.update({'axes.linewidth': 2.0 } )
    plt.rcParams.update({'font.weight'   :'bold'} )



    def xBounds      (self,lim = None, step = __STEP__, step_minor = __STEP_MINOR__):

        if   lim: self.xrange      = lim
        else    : self.xrange      = None 

        self.xstep_major = step
        self.xstep_minor = step_minor

        if self.xrange: self.set_xlim(self.xrange[0], self.xrange[1])

        if not self.xstep_major == __STEP__      :  self.xaxis.set_major_locator( ticker.MultipleLocator( self.xstep_major ) )
        if not self.xstep_minor == __STEP_MINOR__:  self.xaxis.set_minor_locator( ticker.MultipleLocator( self.xstep_minor ) )

        self.xaxis.set_ticks_position('both')


    def yBounds      (self,lim = None, step = __STEP__, step_minor = __STEP_MINOR__):

        if   lim: self.yrange      = lim
        else    : self.yrange      = None 

        self.ystep_major = step
        self.ystep_minor = step_minor

        if self.yrange: self.set_ylim(self.yrange[0], self.yrange[1])

        if not self.ystep_major == __STEP__      :  self.yaxis.set_major_locator( ticker.MultipleLocator( self.ystep_major ) )
        if not self.ystep_minor == __STEP_MINOR__:  self.yaxis.set_minor_locator( ticker.MultipleLocator( self.ystep_minor ) )

        

    def AxisLinewidth(self,axis = ['top', 'bottom', 'left', 'right'], linewidth = __AXISLINEWIDTH__):

        [self.spines[ax].set_linewidth(linewidth) for ax in axis]

    def xlabel(self, name="",fontsize = __AXISFONTSIZE__, theta = 0.0, **kwargs):
        
        if       name == "" and     self.get_xlabel() == "": name_ = ""
        elif     name == "" and not self.get_xlabel() == "": name_ = self.get_xlabel()
        else                                               : name_ = name



        self.set_xlabel(name_ , fontsize = fontsize, rotation = np.pi/180.0 * theta)        
    def ylabel(self, name="",fontsize = __AXISFONTSIZE__, theta = 0.0, **kwargs):
        
        if       name == "" and     self.get_ylabel() == "": name_ = ""
        elif     name == "" and not self.get_ylabel() == "": name_ = self.get_ylabel()
        elif not name == "" and     self.get_ylabel() == "": name_ = name

        self.set_ylabel(name_ , fontsize = fontsize, rotation = np.pi/180.0 * theta)

    def label(self, fontsize = __AXISFONTSIZE__):
        self.set_ylabel(self.get_ylabel(), fontsize= fontsize)
        self.set_xlabel(self.get_xlabel(), fontsize= fontsize)

    def TicksLocator(self):

        
        self.xaxis.set_major_locator(ticker.MultipleLocator(self.xstep_major ))
        self.xaxis.set_minor_locator(ticker.MultipleLocator(self.xstep_minor ))
        self.xaxis.set_ticks_position('both')

        self.yaxis.set_major_locator(ticker.MultipleLocator(self.ystep_major    ))
        self.yaxis.set_minor_locator(ticker.MultipleLocator(self.ystep_minor    ))
        self.yaxis.set_ticks_position('both')

        self.tick_params(which='major',direction='in', length=__MAJORTICKS_LENGTH__, width=__MAJORTICKS_WIDTH__)
        self.tick_params(which='minor',direction='in', length=__MINORTICKS_LENGTH__, width=__MAJORTICKS_WIDTH__)





    def plot(self, x, y, style = Black[0], **kwargs):

        if isinstance(x, list): x = np.array(x).astype(np.float64)

        
        p = super().plot(x, y, linewidth = style.linewidth, color = style.color, dashes    = style.dashes,  **kwargs)
        self.AxisLinewidth()
        self.xlabel("$x$")
        self.ylabel("$y$")
        # self.yaxis.set_label_coords(-0.05,0.50)

        step = 2
        Nminor = 10

        self.xBounds(step = step, step_minor = step/Nminor)
        self.yBounds(step = step, step_minor = step/Nminor)
                
        self.TicksLocator()
        return p



proj.register_projection(MyTemplate)









