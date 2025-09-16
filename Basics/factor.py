'''n = int(input())
num = n+1
i = 1
listt = []
while i <= num:
    if n % i == 0:
        listt.append(i)
        i += 1
    else:
        i += 1
print(listt)
'''
num = int(input())
result = []
for i in range(1,(num//2)+1):
    if num % i == 0:
        result.append(i)
result.append(num)
print(result)