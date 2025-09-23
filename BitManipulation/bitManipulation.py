class Solution:
    def bitManipulation(self, num, i):
        # Code here
        if (num&(1<<(i-1))):
            print(1,end=" ")
        else:
            print(0,end=" ")
        print(num|(1<<(i-1)),end=" ")
        print(num&(~(1<<(i-1))))

num = int(input())
i = int(input())
obj = Solution()
print(obj.bitManipulation(num,i))