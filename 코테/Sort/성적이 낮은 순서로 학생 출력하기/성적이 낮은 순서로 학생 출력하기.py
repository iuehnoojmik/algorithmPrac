n = int(input())
student_list = []

for i in range(n):
    name, grade = input().split()
    grade = int(grade)
    student_list.append((name, grade))

def grade_output(list):
    return list[1]

student_list.sort(key=grade_output)

for name, grade in student_list:
    print(name, end=' ')
