n = int(input())
num = n
result = 0
while num > 0:
    LD = num % 10
    result = (result*10)+LD
    num = num//10
print(num==result)