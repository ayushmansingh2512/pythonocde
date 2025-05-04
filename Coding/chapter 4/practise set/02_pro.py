a = (input("enter the number of students you have : "))

try:
    stu_no = int(a)
    marks = []

    for i in range(stu_no): 
        marksList = int(input(f"enter the marks of student roll no {i+1} : "))
        marks.append(marksList)
    marks.sort()
    print(f"{marks}")
except ValueError:
    print(ValueError)

