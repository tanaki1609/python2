# recursion -  вызов метода самим собой

def func(num):
    if num > 99:
        return
    else:
        num = num + 1
        print(num)
        func(num)

func(0)
