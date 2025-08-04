# tail recursion or backtracking

def func(x,n):
    if n == 0:
        return 
    func(x,n-1)#first call the func 
    print(x)# after calling function print

func(15,4)