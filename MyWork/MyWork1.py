some=[]
while True:
    print("-"*30)
    print("百货购物，欢迎您!")
    print("1.添加您想要的产品。")
    print("2.删除您想要的产品。")
    print("3.修改您想要的产品。")
    print("4.查询您想要的产品。")
    print("5.列出您想要的产品。")
    print("6.退出系统。")
    print("-"*30)
    key=int(input("请选择功能(输入序号1到6):"))
    if key==1:
        print("添加您想要的产品功能")
        name=input("请输入产品名称:")
        soID=input("请输入产品序号(不可重复):")
        hasRecord=False
        for temp in some:
            if temp["ID"]==soID:
                hasRecord=True
                break
        if hasRecord==True:
            print("输入产品序号重复，添加失败！")
            continue
        elif hasRecord==False:
            sing={}
            sing["name"]=name
            sing["ID"]=soID
            some.append(sing)
            print("您订的单已存入购物车!")
            continue
        else:
            print("该产品已卖完，请另找其他产品")            
    elif  key==2:
        print("您选择了删除您想要的产品")
        soID=input("请输入要删除的产品序号:")  
        i=0
        hasRecord=False
        for temp in some:
            if temp["ID"]==soID:
                hasRecord=True
                break
            else:
                i=i+1
        if hasRecord==True:
            del some[i]
            print("删除成功！")
        else:
            print("没有此产品序号，删除失败！") 
    elif key==3:
        print("您选择了修改您想要的产品功能")
        soID=input("请输入你要修改产品序号:")
        hasRecord=False
        for temp in some:
            if temp["ID"]==soID:
                hasRecord=True
                continue
        alterNum=int(input("1.修改产品\n2.退出系统\n"))
        if alterNum==1:
            newName=input("请输入更改好的产品:")
            temp["name"]=newName
            print("产品修改成功")
            continue
        elif alterNum==2:
            continue
        else:
            print("输入错误！请重新输入。")
    elif key==4:
        print("您选择了查询您想要的产品") 
        soID=input("请输入你要查询产品的序号:")
        hasRecord=False
        for temp in some:
            if temp["ID"]==soID:
                hasRecord=True
                break
        if hasRecord==False:
            print("没有此产品的序号，查询失败！")
        else:
            print("序号\t产品")
            print(temp["ID"],"\t",temp["name"])
    elif key==5:
        print("接下来进行遍历所有的产品。")
        print("序号\t产品")
        for temp in some:
            print(temp["ID"],"\t",temp["name"])
    elif key==6:
        quitConfirm=input("确认要退出本系统吗(Y或者N)?")
        if quitConfirm.upper()=="Y":
            print("欢迎使用本系统，谢谢!")
            break        