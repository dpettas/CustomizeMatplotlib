from LineStyle_class import *
from dashes          import *


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
for dash in dashes:
	White .append  ( LineStyle (linewidth = linewidth, color = "#FFFFFF", dashes = dash) ) 
	Black .append  ( LineStyle (linewidth = linewidth, color = "#010101", dashes = dash) ) 
	Red   .append  ( LineStyle (linewidth = linewidth, color = "#F05654", dashes = dash) ) 
	Blue  .append  ( LineStyle (linewidth = linewidth, color = "#5FA2D8", dashes = dash) )
	Orange.append  ( LineStyle (linewidth = linewidth, color = "#F89A2A", dashes = dash) )
	Cyan  .append  ( LineStyle (linewidth = linewidth, color = "#29B2B2", dashes = dash) )
	Green .append  ( LineStyle (linewidth = linewidth, color = "#60BF6E", dashes = dash) )
	Gray  .append  ( LineStyle (linewidth = linewidth, color = "#4E4E4E", dashes = dash) )
