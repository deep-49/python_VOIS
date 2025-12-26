students={}

def addStudent(sid,name,course):
    students[sid]={
        "Name":name,
        "Course":course
    }

def getStudent(sid):
    return students.get(sid)

def getAllStudents():
    return students