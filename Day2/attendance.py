attendance = {}

def putAttendance(sid,days):
    attendance[sid]=days

def attends(sid):
    return attendance.get(sid,0)
