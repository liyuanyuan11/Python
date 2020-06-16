num=[]
nam=[]
while True:
    print("-"*30)
    print("1.请您任意输入两个数字")
    print("2.退出系统")
    try:
        key=int(input("请选择功能(输入序号1到2):"))
    except:
        print("您的输入有误，请输入序号1到2")
        continue
    if key==1:#输入并比较数字。
        try:
            num=int(input("请输入您猜的第一个数字:"))
            nam=int(input("请输入您猜的第二个数字:"))
        except ValueError:
            print("输入错误，输入数字而不是字符，请重试")   
        if num > nam:
            print("第一个数字大于第二个数字")
        if num < nam:
            print("第一个数字小于第二个数字")
        if num == nam:
            print("第一个数字等于第二个数字")
    if key==2:
        quitConfirm=input("确认要退出本系统吗(Y或者N)?")
        if quitConfirm.upper()=="Y":
            print("欢迎使用本系统，谢谢!")
            break
        else:
            print("您输入有误，请重新输入")                    