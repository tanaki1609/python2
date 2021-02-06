# 0,1,1,2,3,5,8,13.......

def fibo(n, a=0, b=1, fib=[]):
    if b <= n:
        fib.append(b)
        a, b = b, a + b
    else:
        return fib
    return fibo(n, a, b, fib)


n = int(input("Enter a number: "))
print(fibo(n))
