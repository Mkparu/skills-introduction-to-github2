score = int(input("Enter your score: "))

if score >= 70:
    grade = 'A'
elif score >= 60:
    grade = 'B'
elif score >= 50:
    grade = 'C'
elif score >= 45:
    grade = 'D'
else:
    grade = 'F'

print("Your grade is", grade)
