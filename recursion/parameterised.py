def func(sum,i,n):
    if i > n:
        print(sum)
        return 
    func(sum+i,i+1,n)

func(0,1,10)