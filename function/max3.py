def maximum_three(a,b,c):
    if a > b and a > c :
        return "A is greater then b and c "
    elif b > a and b > c:
        return "B is greater then a and c"
    else :
        return "C is greater then a and b"
print(maximum_three(2,3,4))