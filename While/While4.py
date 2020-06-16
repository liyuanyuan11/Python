password="338822"
while True:
    userlnput=input("请输入6位密码:")
    if userlnput==password:
        print("打开保险柜")
        break
    else:
        print("您输入的密码不正确，请重新输入:")