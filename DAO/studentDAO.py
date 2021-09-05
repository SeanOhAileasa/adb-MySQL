from mysql.connector import connect
# define class - CStudentDAO
class CStudentDAO: # blueprint state functionality
	nClsAttDB="" # for all instances
	def __init__(self): # initialise object state
		""" Using class attribute to create default value (state).

	Input: object itself (self)
	Process: nClsAttDB
	Output: called automatically when creating a new instance of CStudentDAO
	"""
		self.nClsAttDB=connect(host="localhost",user="root",password="",database="data_representation") # establish a connection
	def fInsMetCreate(self,nInsAttValues):
		""" Using the values (%s) from somewhere passed in as a tuple executing as a variable create record.
	Input: object itself (self); nInsAttValues
	Process: nClsAttDB
	Output: 
	"""		
		nInsObjCursor=self.nClsAttDB.cursor() # traveral over records
		sqlQuery="INSERT INTO student (firstname,age) VALUES (%s,%s)"
		nInsObjCursor.execute(sqlQuery,nInsAttValues) # abstracts away access
		self.nClsAttDB.commit() # commit current transaction
		return nInsObjCursor.lastrowid
	def fInsMetGetAll(self):
		""" Return all records.

	Input: object itself (self)
	Process: nClsAttDB
	Output: show all records
	"""			
		nInsObjCursor=self.nClsAttDB.cursor()
		sqlQuery="SELECT * FROM student"
		nInsObjCursor.execute(sqlQuery)
		return nInsObjCursor.fetchall()
	def fInsMetGetByID(self,nInsAttID):
		""" Using the ID (%s) from somewhere passed in as a tuple executing as a variable find record by ID.

	Input: object itself (self); nInsAttID
	Process: nClsAttDB
	Output: show record by ID
	"""			
		nInsObjCursor=self.nClsAttDB.cursor()
		sqlQuery="SELECT * FROM student WHERE id=%s"
		nTupleValues=(nInsAttID,)
		nInsObjCursor.execute(sqlQuery,nTupleValues)
		return nInsObjCursor.fetchone()
	def fInsMetUpdate(self,nInsAttID):
		""" Using the ID (%s) from somewhere passed in as a tuple executing as a variable update record.

	Input: object itself (self); nInsAttID
	Process: nClsAttDB
	Output: update record by ID
	"""			
		nInsObjCursor=self.nClsAttDB.cursor()
		sqlQuery="UPDATE student SET firstname=%s,age=%s WHERE id=%s"
		nInsObjCursor.execute(sqlQuery,nInsAttID)
		self.nClsAttDB.commit()
	def fInsMetDelete(self,nInsAttID):
		""" Using the values (%s) from somewhere passed in as a tuple executing as a variable delete record.

	Input: object itself (self); nInsAttID
	Process: nClsAttDB
	Output: record deleted
	"""
		nInsObjCursor=self.nClsAttDB.cursor()
		sqlQuery="DELETE FROM student where id=%s"
		nTupleValues=(nInsAttID,)
		nInsObjCursor.execute(sqlQuery,nTupleValues)
		self.nClsAttDB.commit()	