

class LineStyle():
	"""
	arguments:  linewidth, dashes, color, alpha 
	
	"""

	def __init__(self,linewidth,dashes,color, alpha = 1.0, dashDot = [1,1]):
		"""
		Arguments: 
		"""


		self.linewidth = linewidth
		self.dashes    = dashes
		self.color     = color
		self.alpha     = alpha
		self.dashDot   = dashDot
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

	def getColor(self):
		return self.color

	def getLinewidth(self): 
		return self.linewidth


