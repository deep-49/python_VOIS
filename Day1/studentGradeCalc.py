
students = {
    "Amit": [85, 90, 88],
    "Neha": [78, 82, 80],
    "Rahul": [92, 95, 94],
    "Priya": [65, 70, 68],
    "Sonal": [55, 60, 58]
}


def calculate_average(marks):
    return sum(marks) / len(marks)


top_scorer = ""
top_avg = 0


for name, marks in students.items():
    avg = calculate_average(marks)

    if avg >= 90:
        grade = "A"
    elif avg >= 75:
        grade = "B"
    elif avg >= 60:
        grade = "C"
    else:
        grade = "Fail"

    print(f"Name: {name}, Average: {avg:.2f}, Grade: {grade}")

    if avg > top_avg:
        top_avg = avg
        top_scorer = name


print("\nTop Scorer:")
print(f"Name: {top_scorer}, Average Marks: {top_avg:.2f}")
