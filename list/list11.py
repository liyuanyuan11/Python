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