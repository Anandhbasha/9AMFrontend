from db import get_db
from bson.objectid import ObjectId

db = get_db()
collection  = db["NewTable"]
# Add newStudent
def addStudent(data):
    collection.insert_one(data)

# read Data
def getAllStudent():
    return list(collection.find())

# getbyID
def getStudentById(stdId):
    return collection.find_one({"_id":ObjectId(stdId)})
# updateNewStudent
def updateStudent(stdId,updatedData):
    collection.update_one({"_id":ObjectId(stdId)},{"$set":updatedData})

# delete
def deleteStudent(stdId):
    collection.delete_one({"_id":ObjectId(stdId)})