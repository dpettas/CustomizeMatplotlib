
import matplotlib.pyplot as plt
import matplotlib
import numpy  as np
import pandas as pd

from Column  import * 
from sys     import exit
from os.path import isfile

class FileData():
	"""
	Class FileData
	--------------
	
	** filename : absolute path of the filename 
	** columns  : name of the columns that exist in the file
	** action   : "Read" (default) this action read the file data
	** header   : False  (default) if True uses the first line of the csv file 
								to define the column names
	"""

	def __init__(self, filename , columns = "", action = "Read", header = False, skiplines = 0):

		if not isfile(filename): sys.exit("[Error] : The {} does not exist !".format(filename))

		self.filename = filename

		if action.lower() == "read":self._readfile(filename,columns,header,skiplines)
		if action.lower() == "read":self.column = self.__storagecolumns()
	def _readfile        (self,filename,columns,header,skiplines):
		"""
		This method reads the data of the file using the pandas module
		"""

		if columns =="" and header: 
			self.file = pd.read_csv( filename, sep    = "\s+")
			return


		self.file = pd.read_csv( filename, sep    = "\s+", header = None , names  = columns.rstrip().split(),skiprows=skiplines)
	def __storagecolumns  (self                       ):
		column = []

		for col in self.file.columns.values:
			datacol = np.array(self.file[col].values)
			column.append( Column (name = col , data = datacol) )

		return column
	def getColumnNames    (self                       ):

		colnames = []

		for col in self.column: colnames.append(col.name)
		return colnames
	def getNumberofColumns(self                       ): return len(       self.getColumnNames())
	def HasTheSameColumns (self,other                 ): 

		for col in self.getColumnNames():
			if (col not in other.getColumnNames()):
				return False
		return True
		
	def isColumn          (self,colName = ""          ): return colName in self.getColumnNames()
	def colNumber         (self,colName = ""          ):

		for i in range(len(self.column)):
			if self.column[i].name == colName : 
				return i
		print("")
		sys.exit("[Error]: column name {} does not exist.".format(colName) )
	def AddNewColumn      (self,colName = "",data = ""):
		"""
		This method creates a new variable with the same length as the previous columns

		Arguments: 
		colname : the name  of the variable 
		data    : the value of the variable 
		"""
		if self.isColumn(colName): sys.exit("[Error]: column {} is already exist".format(colName))

		self.column.append(Column (name = colName, data = data ) )
	def ReplaceColumn     (self,colName = "",data = ""):
		col = self.colNumber(colName)

		self.column[col].data = data
	def DeleteColumn      (self,colName = ""          ):
		col = self.colNumber(colName)

		del(self.column[col])
	def ReverseColumns    (self                       ):
		out = self
		for col in out.column:
			col.data = col.data[::-1]
		return out
	def __getitem__       (self,colName = ""          ):
		
		val = self.colNumber(colName)
		out = self.column[val].data
		return out
	def __add__           (self,other                 ):
		if not self.HasTheSameColumns(other): sys.exit("The files have not the same columns.")

		out = self
		out.filename = self.filename + " | " + other.filename

		for col in out.getColumnNames():
			selfd  = self [col].tolist()
			otherd = other[col].tolist()

			TotalData = np.array(selfd + otherd)

			out.ReplaceColumn(col, data = TotalData)

		return out


	def size(self):		
		return self.column[0].data.size