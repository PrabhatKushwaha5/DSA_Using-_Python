A = [1, 2, 5, -7, 2, 3]

maxi = -1
summ = 0
temp = []
final = []
for i in range(len(A)):
    if A[i] >= 0:
        summ += A[i]
        temp.append(A[i])
    else:
        
        if (summ > maxi) or (summ == maxi and len(temp) > len(final)):
            maxi = summ
            final = temp[:]
        summ = 0
        temp = []


if (summ > maxi) or (summ == maxi and len(temp) > len(final)):
    final = temp[:]

print(final)
