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