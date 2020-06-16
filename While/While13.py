num=97
while True:
    num=int(input("请输入您猜的数字！"))
    if num < 892:
        print("要大一些！")
    if num > 892:
        print("要小一些！")
    if num == 892:
        print("猜对了，您好棒！")
        break    