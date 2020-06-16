studentList=[]
student={}
student={"name":"李若瑜","ID":"1","score1":95,"score2":100,"score3":96,"total":291}
studentList.append(student)
student={"name":"张子栋","ID":"2","score1":93,"score2":100,"score3":95,"total":288}
studentList.append(student)
student={"name":"王小明","ID":"3","score1":100,"score2":94,"score3":100,"total":294}
studentList.append(student)
print("现在已经有"+str(len(studentList))+"位同学的成绩，他们的得分入下：")
print("学号  姓名  语文  数学  英语  总分")
print(studentList[0].get("ID")," ",studentList[0].get("name")," ",studentList[0].get("score1")," ",studentList[0].get("score2")," ",studentList[0].get("score3")," ",studentList[0].get("total"))
print(studentList[1].get("ID")," ",studentList[1].get("name")," ",studentList[1].get("score1")," ",studentList[1].get("score2")," ",studentList[1].get("score3")," ",studentList[1].get("total"))
print(studentList[2].get("ID")," ",studentList[2].get("name")," ",studentList[2].get("score1")," ",studentList[2].get("score2")," ",studentList[2].get("score3")," ",studentList[2].get("total"))
studentList[1]["score2"]=98
studentList[1]["total"]=studentList[1]["score1"]+studentList[1]["score2"]+studentList[1]["score3"]
print("第2位同学的语文成绩录入有误，要改为98分")
print("第2位同学修改后的成绩如下")
print("学号  姓名  语文  数学  英语  总分")
print(studentList[1].get("ID")," ",studentList[1].get("name")," ",studentList[1].get("score1")," ",studentList[1].get("score2")," ",studentList[1].get("score3")," ",studentList[1].get("total"))
print("接下来要录入一位新同学的成绩")
student={}
student["name"]=input("请输入学生姓名:")
student["ID"]=input("请输入学生学号:")
student["score1"]=input("请输入学生语文成绩:")
student["score2"]=input("请输入学生数学成绩:")
student["score3"]=input("请输入学生英语成绩:")
student["total"]=float(student["score1"])+float(student["score2"])+float(student["score3"])
studentList.append(student)
print("现在已经有"+str(len(studentList))+"位同学的成绩，他们的得分入下：")
print("学号  姓名  语文  数学  英语  总分")
print(studentList[0].get("ID")," ",studentList[0].get("name")," ",studentList[0].get("score1")," ",studentList[0].get("score2")," ",studentList[0].get("score3")," ",studentList[0].get("total"))
print(studentList[1].get("ID")," ",studentList[1].get("name")," ",studentList[1].get("score1")," ",studentList[1].get("score2")," ",studentList[1].get("score3")," ",studentList[1].get("total"))
print(studentList[2].get("ID")," ",studentList[2].get("name")," ",studentList[2].get("score1")," ",studentList[2].get("score2")," ",studentList[2].get("score3")," ",studentList[2].get("total"))
print(studentList[3].get("ID")," ",studentList[3].get("name")," ",studentList[3].get("score1")," ",studentList[3].get("score2")," ",studentList[3].get("score3")," ",studentList[3].get("total"))