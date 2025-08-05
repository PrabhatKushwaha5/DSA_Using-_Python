n = int(input())
even_sum = 0
odd_sum = 0
while n>0:
    digit = n%10
    if digit % 2 == 0:
        even_sum += digit
    else:
        odd_sum += digit
    n = n//10
print(odd_sum,even_sum) 