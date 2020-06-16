choice=input("是否需要输入新的学生信息(Yes/Y表示需要需要录入)?")
studentList=[]
if choice.upper()=="YES" or choice.upper()=="Y":
    isError=False
    student={}
    student["name"]=input("请输入姓名:")
    student["ID"]=input("请输入学号:")
    score1=float(input("请输入语文成绩:"))
    if score1 <= 100 and score1 >= 0:
        student["score1"]=score1
    else:
        print("输入的语文成绩有错误!")
        isError=True
    score2=float(input("请输入数学成绩:"))
    if score2 <= 100 and score2 >= 0:
        student["score2"]=score2
    else:
        print("输入的数学成绩有错误!")
        isError=True
    score3=float(input("请输入英语成绩:"))
    if score3 <= 100 and score3 >= 0:
        student["score3"]=score3
    else:
        print("输入的英语成绩有错误!")
        isError=True  
    if isError==False:
        student["total"]=student["score1"]+student["score2"]+student["score3"]
        studentList.append(student)
        print(student["name"]+"的成绩录入成功!")
    else:
        print("输入有误，录入成绩失败!")    