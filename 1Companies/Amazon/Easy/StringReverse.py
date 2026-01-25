class solution:
    def solve(self,A):
        words = A.split()
        words.reverse()
        return " ".join(words)
    

A = input().strip()
sol = solution()
result = sol.solve(A)
print(result)
