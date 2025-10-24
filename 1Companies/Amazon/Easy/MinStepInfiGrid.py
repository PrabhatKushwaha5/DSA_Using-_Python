class Solution:
    def coverPoints(self, A, B):
        steps = 0
        for i in range(1, len(A)):
            dx = abs(A[i] - A[i - 1])
            dy = abs(B[i] - B[i - 1])
            steps += max(dx, dy)
        return steps

# ------------------- Driver Code -------------------
if __name__ == "__main__":
    # Example input
    A = [0, 1, 1]
    B = [0, 1, 2]
    
    sol = Solution()
    result = sol.coverPoints(A, B)
    print(result)  # Output: 2
