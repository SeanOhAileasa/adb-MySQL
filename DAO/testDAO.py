from studentDAO import CStudentDAO

# instantiate object - CStudentDAO
nInsObjStudent=CStudentDAO()

nLatestID=nInsObjStudent.fInsMetCreate(("Mark",45)) # test CRUD Create
nCurrentID=nInsObjStudent.fInsMetGetByID(nLatestID) # test CRUD Read(id)
print(nCurrentID)
nInsObjStudent.fInsMetUpdate(("Fred",21,nLatestID)) # test CRUD Update
nCurrentID=nInsObjStudent.fInsMetGetByID(nLatestID) # test CRUD Read(id)
print(nCurrentID)
nAllStudents=nInsObjStudent.fInsMetGetAll() # test CRUD Read(*)
for nEachStudent in nAllStudents:
	print(nEachStudent)
nInsObjStudent.fInsMetDelete(nLatestID) # test CRUD Delete