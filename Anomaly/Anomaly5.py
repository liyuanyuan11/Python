try:
    numberEight=8
    print(numberEight/0)
    print("没有出现异常，一切顺利")
except ZeroDivisionError:
    print("这是一个除零错误")