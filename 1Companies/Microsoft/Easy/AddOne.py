class Solution:
    
    def plusOne(self, A):
        # list -> string
        num_str = ""
        for digit in A:
            num_str += str(digit)

        # string -> int -> +1
        num = int(num_str) + 1

        # int -> string
        num_str = str(num)

        # string -> list
        result = []
        for ch in num_str:
            result.append(int(ch))

        return result


# -------- Driver Code --------
if __name__ == "__main__":
    A = list(map(int, input().split()))
    obj = Solution()
    print(obj.plusOne(A))
