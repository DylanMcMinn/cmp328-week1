mark = int(input("Enter mark (0-100): "))
if mark >=70:
    grade = "First"
elif mark>=60:
    grade = "Upper Second"
elif mark>=50:
    grade = "Lower Second"
else:
    grade = "Fail"
print("Grade:", grade)