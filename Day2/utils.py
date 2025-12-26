import datetime as d
# import math

def currentDate():
    return d.datetime.now()

def percentage(total, max_marks):
    return (total / max_marks) * 100

def moduleInfo():
    print("===================================\n")
    print("Module Name :", __name__)
    print("File Name   :", __file__)
    print("Dictionary  :", __dict__)
    print("===================================\n")