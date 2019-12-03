from my_mpl_template.linestyle        import *
from my_mpl_template.linestyle.dashes import *


White = []
Black = []
Red   = []
Blue  = []
Orange= []
Cyan  = []
Green = []
Gray  = []



linewidth = 3.0
Default     = LineStyle (linewidth = linewidth, color = "#010101", dashes = [])
for d in dash:
	White .append  ( LineStyle (linewidth = linewidth, color = "#FFFFFF", dashes = d) ) 
	Black .append  ( LineStyle (linewidth = linewidth, color = "#010101", dashes = d) ) 
	Red   .append  ( LineStyle (linewidth = linewidth, color = "#F05654", dashes = d) ) 
	Blue  .append  ( LineStyle (linewidth = linewidth, color = "#5FA2D8", dashes = d) )
	Orange.append  ( LineStyle (linewidth = linewidth, color = "#F89A2A", dashes = d) )
	Cyan  .append  ( LineStyle (linewidth = linewidth, color = "#29B2B2", dashes = d) )
	Green .append  ( LineStyle (linewidth = linewidth, color = "#60BF6E", dashes = d) )
	Gray  .append  ( LineStyle (linewidth = linewidth, color = "#CCCCCC", dashes = d) )
