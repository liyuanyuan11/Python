nameList=["李若瑜","长子栋","王小明"]
IDList=["1","2","3"]
scoreList1=[94,100,99]
scoreList2=[93,100,95]
scoreList3=[100,94,100]
totalList=[scoreList1[0]+scoreList2[0]+scoreList3[0],scoreList1[1]+scoreList2[1]+scoreList3[1],scoreList1[2]+scoreList2[2]+scoreList3[2]]
print("现在已经有"+str(len(nameList))+"位同学的成绩，他们的得分如下:")
print("学号  姓名  语文  数学  英语  总分")
print(IDList[0]," ",nameList[0]," ",scoreList1[0]," ",scoreList2[0]," ",scoreList3[0]," ",totalList[0])
print(IDList[1]," ",nameList[1]," ",scoreList1[1]," ",scoreList2[1]," ",scoreList3[1]," ",totalList[1])
print(IDList[2]," ",nameList[2]," ",scoreList1[2]," ",scoreList2[2]," ",scoreList3[2]," ",totalList[2])
print("第二位同学的语文成绩录入有误，要改为98分")
scoreList2[1]=98
totalList[1]=scoreList1[1]+scoreList2[1]+scoreList3[1]
print("第二位同学修改后的成绩如下：")
print("学号  姓名  语文  数学  英语  总分")
print(IDList[1]," ",nameList[1]," ",scoreList1[1]," ",scoreList2[1]," ",scoreList3[1]," ",totalList[1])
print("接下来要录入一位新同学的成绩")
nameList.append(input("请输入学生姓名："))
IDList.append(input("请输入学生学号："))
scoreList1.append(input("请输入学生语文成绩："))
scoreList2.append(input("请输入学生数学成绩："))
scoreList3.append(input("请输入学生英语成绩："))
totalList.append(float(scoreList1[3])+float(scoreList2[3])+float(scoreList3[3]))
print("现在已经有"+str(len(nameList))+"位同学的成绩，他们的得分如下：")
print("学号  姓名  语文  数学  英语  总分")
print(IDList[0]," ",nameList[0]," ",scoreList1[0]," ",scoreList2[0]," ",scoreList3[0]," ",totalList[0])
print(IDList[1]," ",nameList[1]," ",scoreList1[1]," ",scoreList2[1]," ",scoreList3[1]," ",totalList[1])
print(IDList[2]," ",nameList[2]," ",scoreList1[2]," ",scoreList2[2]," ",scoreList3[2]," ",totalList[2])
print(IDList[3]," ",nameList[3]," ",scoreList1[3]," ",scoreList2[3]," ",scoreList3[3]," ",totalList[3])
print("现在要将王小明同学的记录从列表中删除")
input=nameList.index("王小明")
del nameList[input],IDList[input],scoreList1[input],scoreList2[input],scoreList3[input],totalList[input]
print("现在已经有"+str(len(nameList))+"位同学的成绩，他们的得分入下：")
print("学号  姓名  语文  数学  英语  总分")
print(IDList[0]," ",nameList[0]," ",scoreList1[0]," ",scoreList2[0]," ",scoreList3[0]," ",totalList[0])
print(IDList[1]," ",nameList[1]," ",scoreList1[1]," ",scoreList2[1]," ",scoreList3[1]," ",totalList[1])
print(IDList[2]," ",nameList[2]," ",scoreList1[2]," ",scoreList2[2]," ",scoreList3[2]," ",totalList[2])