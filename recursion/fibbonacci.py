def fib(i):
    if i == 0:
        return 0
    if i == 1:
        return 1
    return fib(i-1)+fib(i-2)

def func(n,i):
    if i > n:
        return 
    print(fib(i),end=" ")
    func(n,i+1)


func(10,0)