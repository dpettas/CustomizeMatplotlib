

class LineStyle():
    """
    arguments:  linewidth, dashes, color, alpha 
        
    """

    def __init__(self,linewidth,dashes,color, symbol = 'o', size=10,
            alpha = 1.0, dashDot = [1,1]):
        """
        Arguments: 
        """

        # variables related with the plot
        self.linewidth = linewidth
        self.dashes    = dashes
        self.color     = color
        self.alpha     = alpha
        self.dashDot   = dashDot

        # variables related with the scatter
        self.symbol    = symbol
        self.size      = size

    def DashDot(self):
        """
        it is used for the cases where I want to change the dashes along a line 
        for example in case where a hysteresis loop can be observed
        """
        return LineStyle (linewidth = self.linewidth,
                          color     = self.color    ,
                          alpha     = self.alpha    , 
                          dashDot   = self.DashDot)

    def setLineWidth(self,linewidth):
        self.linewidth = linewidth
        return self

    def setColor(self, color):
        self.color = color
        return self
#<><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><>
# GETTERS
#<><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><>
    def get_color    (self): return self.color
    def get_linewidth(self): return self.linewidth
    def get_dashes   (self): return self.dashes 
    def get_symbol   (self): return self.symbol
    def get_size     (self): return self.size
#<><><><><><><><><><><><><><><><><><>
# These methods should be depreciated
#<><><><><><><><><><><><><><><><><><>
    def getColor    (self): return self.color
    def getLinewidth(self): return self.linewidth
        
















