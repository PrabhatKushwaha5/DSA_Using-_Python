def PascleTriangle(n):
    tri = []
    for i in range(n):
        row = [1]
        if i>0:
            last_row = tri[i-1]
            for j in range(1,i):
                row.append(last_row[j-1]+last_row[j])
            row.append(1)
        tri.append(row)
    return tri

n = int(input("Enter number of rows for Pascal's Triangle: "))
triangle = PascleTriangle(n)

print("\nPascal's Triangle:")
for row in triangle:
    
    print(" "*(n-len(row)), end="") 
    print(" ".join(map(str, row)))
