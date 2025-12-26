from student import getStudent
from attendance import attends
from marks import mark
from fees import getFee
from utils import percentage
import datetime
class Report:

    def generate(self, sid):
        student = getStudent(sid)

        if student is None:
            print("Student not found")
            return
        
        marks_dict = mark(sid)
       
        if marks_dict:
             total_marks = sum(marks_dict.values()) 
        else :
            return 0
        
        percent = percentage(total_marks, 300) 

        print("\n========== STUDENT REPORT ==========")
        print("Student ID :", sid)
        print("Name       :", student["Name"])
        print("Course     :", student["Course"])
        print("Attendance :", attends(sid), "days")
        print("Marks      :", mark(sid))
        print("Fees Paid  :", getFee(sid))
        print("percentage :",percent,"%")
        print(datetime.datetime.now())
        print("===================================\n")