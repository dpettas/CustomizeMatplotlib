from   my_mpl_template.myFigure         import *
from   my_mpl_template.linestyle        import * 
from   my_mpl_template.template         import *
from   my_mpl_template.rcParams         import *
from   my_mpl_template                  import rcParams
from   my_mpl_template.linestyle.dashes import *



White = []
Black = []
Red   = []
Blue  = []
Orange= []
Cyan  = []
Green = []
Gray  = []








def graph_mode(mode = "publication"):
	"""
	THIS FUNCTION MUST BE INITIALIZED AT THE BEGINING OF THE SCRIPT
	TO USE THE DEFINED PARAMETERS FOR PLOTING
	
	args: 
	mode = "publication" or "presentation"
	"""


	rcParams.graph_mode(mode)
	
	
	global White, Black, Blue, Red, Orange, Cyan, Green, Gray


	if   mode.lower() == "publication" : 
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
			Gray  .append  ( LineStyle (linewidth = linewidth, color = "#4E4E4E", dashes = d) )

	elif mode.lower() == "presentation": 
		linewidth = 3.5

		Default     = LineStyle (linewidth = linewidth, color = "#010101", dashes = [])
		for d in dash:
			White .append  ( LineStyle (linewidth = linewidth, color = "#FFFFFF", dashes = d) ) 
			Black .append  ( LineStyle (linewidth = linewidth, color = "#010101", dashes = d) ) 
			Red   .append  ( LineStyle (linewidth = linewidth, color = "#F05654", dashes = d) ) 
			Blue  .append  ( LineStyle (linewidth = linewidth, color = "#5FA2D8", dashes = d) )
			Orange.append  ( LineStyle (linewidth = linewidth, color = "#F89A2A", dashes = d) )
			Cyan  .append  ( LineStyle (linewidth = linewidth, color = "#29B2B2", dashes = d) )
			Green .append  ( LineStyle (linewidth = linewidth, color = "#60BF6E", dashes = d) )
			Gray  .append  ( LineStyle (linewidth = linewidth, color = "#4E4E4E", dashes = d) )

