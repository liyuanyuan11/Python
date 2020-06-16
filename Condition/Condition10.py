student=float(input("请输入的学生成绩:"))
if student <= 80:
    print("你的成绩不及格!")
elif student >= 80 and student <= 89:
    print("你的成绩及格!")
elif student >= 90 and student <= 99:
    print("你的成绩良好!")
elif student >= 100 and student <= 109:
    print("你的成绩优秀!")
elif student >= 110:
    print("你的成绩100分!")
