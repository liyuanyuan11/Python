studentList=[]
while True:
    print("-"*30)
    print("学生成绩系统")
    print("1.添加学生的信息")
    print("2.删除学生的信息")
    print("3.修改学生的信息")
    print("4.查询学生的信息")
    print("5.列出所有学生的信息")
    print("6.退出系统")
    print("-"*30)
    try:
        key=int(input("请选择功能(输入序号1到6):"))
    except:
        print("您的输入有误，请输入序号1到6")
        continue
    if key==1:
        print("您选择了添加学生的信息功能")
        name=input("请输入姓名:")
        stuld=input("请输入学号(不可重复):")
        hasRecord=False
        for temp in studentList:
            if temp["ID"]==stuld:
                hasRecord=True
                break  
        if hasRecord==True:
            print("输入学号重复，添加失败！")
            continue
        else:
            student={}
            student["name"]=name
            student["ID"]=stuld
            try:
                score1=float(input("请输入语文成绩:"))
            except:
                print("输入的不是数字，添加失败！") 
                continue
            if score1 <= 100 and score1 >= 0:
                student["score1"]=score1
            else:
                print("输入的语文成绩有错误!")
                continue
            try:
                score2=float(input("请输入数学成绩:"))
            except:
                print("输入的不是数字，添加失败！") 
                continue
            if score2 <= 100 and score2 >= 0:
                student["score2"]=score2
            else:
                print("输入的数学成绩有错误!")
                continue
            try:
                score3=float(input("请输入英语成绩:"))
            except:
                print("输入的不是数字，添加失败！") 
                continue
            if score3 <= 100 and score3 >= 0:
                student["score3"]=score3
            else:
                print("输入的英语成绩有错误!")
                continue
            student["total"]=student["score1"]+student["score2"]+student["score3"]
            studentList.append(student)
            print(student["name"]+"的成绩录入成功!")
    elif key==2:
        print("您选择了删除学生信息功能")
        stuld=input("请输入要删除的学号:")
        i=0
        hasRecord=False
        for temp in studentList:
            if temp["ID"]==stuld:
                hasRecord=True
                break
            else:
                i=i+1
        if hasRecord==True:
            del studentList[i]
            print("删除成功！")
        else:
            print("没有此学生学号，删除失败！")
    elif key==3:
        print("您选择了修改学生信息功能")
        stuld=input("请输入你要修改学生的学号:")
        hasRecord=False
        for temp in studentList:
            if temp["ID"]==stuld:
                hasRecord=True
                continue
        if hasRecord==False:
            print("没有此学号，修改失败!")
        else:
            while True:
                try:
                    alterNum=int(input("1.修改姓名\n2.修改学号\n3.修改语文成绩\n4.修改数学成绩\n5.修改英语成绩\n6.退出修改\n"))
                except:
                    print("输入有误，请输入编号1到6")
                    continue
                if alterNum==1:
                    newName=input("请输入更改好的姓名:")
                    temp["name"]=newName
                    print("姓名修改成功")
                    continue
                elif alterNum==2:
                    newld=input("请输入更改后的学号:")
                    hasSameID=False
                    for temp1 in studentList:
                        if temp1["ID"]==newld:
                            hasSameID=True
                            continue
                    if hasSameID==True:
                        print("输入学号不可重复，修改失败!")
                    else:
                        temp["ID"]=newld
                        print("学号修改成功!")
                    continue
                elif alterNum==3:
                    score1=float(input("请输入更改后的语文成绩:"))
                    if score1 <= 100 and score1 >= 0:
                        temp["score1"]=score1
                        temp["total"]=temp["score1"]+temp["score2"]+temp["score3"]
                        print("语文成绩修改成功!")
                    else:
                        print("输入的语文成绩有错误，修改失败!")
                    continue             
                elif alterNum==4:
                    try:
                        score2=float(input("请输入更改后的数学成绩:"))
                    except:
                        print("输入的不是数字，修改失败!")
                        break
                    if score2 <= 100 and score2 >= 0:
                            temp["score2"]=score2
                            temp["total"]=temp["score1"]+temp["score2"]+temp["score3"]
                            print("数学成绩修改成功!")
                    else:
                        print("输入的数学成绩有错误，修改失败!")
                        continue
                elif alterNum==5:
                    try:
                        score3=float(input("请输入更改后的英语成绩:"))
                    except:
                        print("输入的不是数字，修改失败!")
                        break
                    if score3 <= 100 and score3 >= 0:
                            temp["score3"]=score3
                            temp["total"]=temp["score1"]+temp["score2"]+temp["score3"]
                            print("英语成绩修改成功!")
                    else:
                        print("输入的英语成绩有错误，修改失败!")
                        continue
                elif alterNum==6:
                    break
                else:
                    print("输入错误！请重新输入。")
    elif key==4:
        print("您选择了查询学生信息功能") 
        stuld=input("请输入你要查询学生的学号:")
        hasRecord=False
        for temp in studentList:
            if temp["ID"]==stuld:
                hasRecord=True
                break
        if hasRecord==False:
            print("没有此学生学号，查询失败！")
        else:
            print("学号 \t 姓名 \t 语文 \t 数学 \t 英语 \t 总分")
            print(temp["ID"],"\t",temp["name"],"\t",temp["score1"],"\t",temp["score2"],"\t",temp["score3"],"\t",temp["total"])
    elif key==5:
        print("接下来进行遍历所有的学生信息。")
        print("学号 \t 姓名 \t 语文 \t 数学 \t 英语 \t 总分")
        for temp in studentList:
            print(temp["ID"],"\t",temp["name"],"\t",temp["score1"],"\t",temp["score2"],"\t",temp["score3"],"\t",temp["total"])
    elif key==6:
        quitConfirm=input("确认要退出本系统吗(Y或者N)?")
        if quitConfirm.upper()=="Y":
            print("欢迎使用本系统，谢谢!")
            break
        else:
            print("您输入有误，请重新输入")