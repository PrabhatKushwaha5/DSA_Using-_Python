#if variable have same value then it shows same address
x = 100
print(id(x))
x = 100
print(id(x))
x = 200
print(id(x))

