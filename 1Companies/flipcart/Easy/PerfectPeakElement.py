class Solution:
    def perfectPeak(self, A):
        N = len(A)
        if N < 3:
            return 0
        left_max = [0] * N
        left_max[0] = A[0]
        for i in range(1, N):
            left_max[i] = max(left_max[i-1], A[i])
        right_min = [0] * N
        right_min[N-1] = A[N-1]
        for i in range(N-2, -1, -1):
            right_min[i] = min(right_min[i+1], A[i])
        for i in range(1, N-1):
            if A[i] > left_max[i-1] and A[i] < right_min[i+1]:
                return 1
        return 0


if __name__ == "__main__":
    A = list(map(int, input("Enter array elements: ").split()))
    sol = Solution()
    result = sol.perfectPeak(A)
    print(result)
