

class LineStyle():
	"""
	arguments:  linewidth, dashes, color, alpha 
	
	"""

	def __init__(self,linewidth,dashes,color, alpha = 1.0):
		self.linewidth = linewidth
		self.dashes    = dashes
		self.color     = color
		self.alpha     = alpha
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


