import matplotlib.pyplot    as plt

class LineStyle():
	"""
	Declare Colors: 
									White, Black, Red, Blue, Orange, Cyan, Green, Gray
  Dashes        : 0-5
	"""

	def __init__(self,linewidth,dashes,color):
		self.linewidth = linewidth
		self.dashes    = dashes
		self.color     = color

	def DashDot(self):
		return LineStyle (linewidth = self.linewidth, color = self.color, dashes = [1,1])

	def setLineWidth(self,linewidth):
		self.linewidth = linewidth
		return self

	def setColor(self, color):
		self.color = color
		return self

	def getColor(self):
		return self.color

	def getLinewidth(self): 
		return self.linewidth



White = []
Black = []
Red   = []
Blue  = []
Orange= []
Cyan  = []
Green = []
Gray  = []


dashes   = []
dashes.append( []                     ) # dash 0: solid line
dashes.append( [2,2]                  ) # dash 1
dashes.append( [4,2]                  ) # dash 2
dashes.append( [1,2,10,2]             ) # dash 3
dashes.append( [1,1,1,1,10,1]         ) # dash 5
dashes.append( [1,1,1,1,1,1,1,1,10,1] ) # dash 5


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

