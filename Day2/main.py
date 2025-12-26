from student import addStudent
from attendance import putAttendance
from marks import calMarks
from fees import pay
from report import Report


def main():
    sid = int(input("Enter Student ID: "))
    name = input("Enter Name: ")
    course = input("Enter Course: ")

    addStudent(sid, name, course)

    days = int(input("Enter Attendance Days: "))
    putAttendance(sid, days)

    calMarks(sid, "Python", int(input("Python Marks: ")))
    calMarks(sid, "DBMS", int(input("DBMS Marks: ")))
    calMarks(sid, "Maths", int(input("Maths Marks: ")))

    amount = int(input("Enter Fees Paid: "))
    pay(sid, amount)

    rpt = Report()
    rpt.generate(sid)

if __name__ == "__main__":
    main()