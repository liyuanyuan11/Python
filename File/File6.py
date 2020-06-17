def LoadFromText(sList):
    print("加载已有数据……")
    try:
        txtFile=open("/Users/chenchaoyang/Desktop/python/Python/File/students.txt","r")
        while True:
            line=txtFile.readline()
            if not line or line.strip()==" ":
                break
            else:
                s=line.split(" ")
                stu=Student()
                stu.ID=s[0]
                stu.name=s[1]
                stu.score1=float(s[2])
                stu.score2=float(s[3])
                stu.score3=float(s[4])
                stu.total=float(s[5])
                sList.append(stu)
    except:
        txtFile=open("/Users/chenchaoyang/Desktop/python/Python/File/students.txt","w")
        txtFile.close()
        print("加载成功!")
def AddToText(stu):
    txtFile=open("/Users/chenchaoyang/Desktop/python/Python/File/students.txt","a")
    txtFile.write(stu.ID)
    txtFile.write(" ")
    txtFile.write(stu.name)
    txtFile.write(" ")
    txtFile.write(str(stu.score1))   
    txtFile.write(" ")
    txtFile.write(str(stu.score2))
    txtFile.write(" ")
    txtFile.write(str(stu.score3))
    txtFile.write(" ")
    txtFile.write(str(stu.total))
    txtFile.write("\n")
    print(stu)
    txtFile.close()
def WriteToText(sList):
    txtFile=open("/Users/chenchaoyang/Desktop/python/Python/File/students.txt","w")
    for stu in sList:
        txtFile.write(stu.ID)
        txtFile.write("")
        txtFile.write(stu.name)
        txtFile.write("")
        txtFile.write(str(stu.score1))   
        txtFile.write("")
        txtFile.write(str(stu.score2))
        txtFile.write("")
        txtFile.write(str(stu.score3))
        txtFile.write("")
        txtFile.write(str(stu.total))
        txtFile.write("\n")
    txtFile.close()
class Student:
    def __init__(self):
        self.name=""
        self.ID=""
        self.score1=0
        self.score2=0
        self.score3=0   
        self.total=0 
    def getSum(self):
        self.total=self.score1+self.score2+self.score3
    def printStudent(self):
        print(self.ID,"\t",self.name,"\t",self.score1,"\t",self.score2,"\t",self.score3,"\t",self.total)
def hasRecord(sList,sID):
    result=-1
    i=0
    for temp in sList:
        if temp.ID==sID:
            result=i
            break 
        else:
            i=i+1
    return result 
def getScore(subject,action):
    try:
        score=float(input("请输入"+subject+"成绩:")) 
    except:
        print("输入的不是数字,"+subject+"失败!")
        return -1
    if score <= 100 and score >= 0:
        return score
    else:
        print("输入的"+subject+"成绩有错误,"+action+"失败!") 
        return -1  
def showInfo():
    print("-"*30)
    print("学生成绩系统")
    print("1.添加学生的信息")
    print("2.删除学生的信息")
    print("3.修改学生的信息")
    print("4.查询学生的信息")
    print("5.列出所有学生的信息")
    print("6.退出系统")
def updateStudent(sList,student):
    while True: 
        try:
            alterNum=int(input("1.修改姓名\n2.修改学号\n3.修改语文成绩\n4.修改数学成绩\n5.修改英语成绩\n6.退出修改\n"))
        except:
            print("输入有误,请输入编号1到6")
            continue
        if alterNum==1:
            newName=input("请输入更改好的姓名:")
            student.name=newName
            print("姓名修改成功")
            continue
        elif alterNum==2:
            newld=input("请输入更改后的学号:")
            newlndex=hasRecord(student,newld)
            if newlndex >-1:
                print("输入学号不可重复，修改失败!")
            else:
                student.ID=newld
                print("学号修改成功")
            continue
        elif alterNum==3:
            score1=getScore("语文","修改")
            if score1>-1:
                student.score1=score1
                student.getSum()
                print("语文成绩修改成功!")
            continue
        elif alterNum==4:
            score2=getScore("数学","修改")
            if score2>-1:
                student.score2=score2
                student.getSum()
                print("数学成绩修改成功!")
            continue                               
        elif alterNum==5:
            score3=getScore("英语","修改")
            if score3>-1:
                student.score3=score3
                student.getSum()
                print("英语成绩修改成功!")
            continue
        elif alterNum==6:
            break
        else:
            print("输入错误请重新输入！")
    print(sList)
    WriteToText(sList)
studentList=[]
LoadFromText(studentList)
while True:
    showInfo()
    try:
        key=int(input("请选择功能(输入序号1到6):"))
    except:
        print("您的输入有误，请输入序号1到6")
        continue
    if key==1:
        print("您选择了添加学生信息功能")
        name=input("请输入姓名:")
        stuId=input("请输入学号（不可重复）:")
        index=hasRecord(studentList,stuId)
        if index >- 1:
            print("输入学号重复，添加失败!")
            continue
        else:
            newStudent = Student()
            newStudent.name = name
            newStudent.ID = stuId
            score1=getScore("语文","添加")
            if score1 >- 1:
                newStudent.score1 = score1
            else:
                continue
            score2=getScore("数学","添加")
            if score2 >- 1:
                newStudent.score2 = score2
            else:
                continue
            score3=getScore("英语","添加")
            if score3 >- 1:
                newStudent.score3 = score3
            else:
                continue
            newStudent.getSum()
            studentList.append(newStudent)
            AddToText(newStudent)
            print(newStudent.name + "的成绩录入成功！")
    elif key == 2:
        print("您选择了删除学生信息功能")
        stuId=input("请输入要删除的学号:")
        index=hasRecord(studentList,stuId)
        if index >- 1:
            del studentList[index]
            WriteToText(studentList)
            print("删除成功!")
        else:
            print("没有此学生学号，删除失败!") 
    elif key == 3:
        print("您选择了修改学生信息功能")
        stuId=input("请输入你要修改学生的学号:")
        index=hasRecord(studentList,stuId)
        if index == -1:
            print("没有此学号，修改失败!")
        else:
            temp=studentList[index]
            updateStudent(studentList,temp)
    elif key == 4: 
        print("您选择了查询学生信息功能")
        stuId=input("请输入你要查询学生的学号:")
        index=hasRecord(studentList,stuId)
        if index == -1:
            print("没有此学生学号，查询失败!")
        else:
            temp=studentList[index]
            print("学号\t姓名\t语文\t数学\t英语\t总分")     
            temp.printStudent()
    elif key == 5:
        print("接下来进行遍历所有的学生信息…")
        print("学号\t姓名\t语文\t数学\t英语\t总分")
        for temp in studentList:
            temp.printStudent()
    elif key==6:
        quitConfirm=input("确认要退出本系统吗(Y或者N)?")
        if quitConfirm.upper()=="Y":
            print("欢迎使用本系统，谢谢!")
            break
        else:
            print("您输入有误，请重新输入!")                                    