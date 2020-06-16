while True:
    try:
        firstNumber=int(input("请输入一个不为零的数字："))
        secondNumber=10/firstNumber
        print(secondNumber)
        print("没有出现任何异常")
        break
    except ZeroDivisionError:
        print("输入错误，0不可以作为除数，请重试")
    except ValueError:
        print("输入错误，输入数字而不是字符，请重试")