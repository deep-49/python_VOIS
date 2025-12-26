marks={}

def calMarks(sid,subject,score):
    if sid not in marks:
        marks[sid]={}
    marks[sid][subject]=score

def getMarks(sid,subject):
    if sid not in marks:
        return 0
    
    return sum(marks[sid].value())
def mark(sid):
    return marks.get(sid,{})
    
