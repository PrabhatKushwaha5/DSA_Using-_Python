class Solution(object):
    def getRow(self, A):
        tri = []
        for i in range(A+1):
            row = [1]
            if i > 0:
                last_row = tri[i-1]
                for j in range(1, i):
                    row.append(last_row[j-1] + last_row[j])
                row.append(1)
            tri.append(row)
        return tri[A]

A = int(input("Enter row number: ").strip())

print(Solution().getRow(A))

