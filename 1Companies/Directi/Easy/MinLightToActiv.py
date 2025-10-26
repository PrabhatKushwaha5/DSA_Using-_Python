class Solution:
    def solve(self, A, B):
        n = len(A)
        i = 0
        count = 0
        while i < n:
            light = -1
            left = max(0, i - B + 1)
            right = min(n - 1, i + B - 1)
            for j in range(right, left - 1, -1):
                if A[j] == 1:
                    light = j
                    break
            if light == -1:
                return -1
            count += 1
            i = light + B
        return count


if __name__ == "__main__":
    A = list(map(int, input("Enter array elements (0 or 1): ").split()))
    B = int(input("Enter power of light (B): "))
    sol = Solution()
    print(sol.solve(A, B))
