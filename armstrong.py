n = int(input())
num = n
total = 0
nod = len(str(num))

while num > 0:
    LD = num%10
    total = total + (LD**nod)
    num = num//10
print(total == n)