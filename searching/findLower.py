class Solution:
    def findFloor(self, arr, x):
        # code here
        n = len(arr)
        low = 0
        high = n-1
        index = -1
        while low<=high:
            mid = (low+high)//2
            if arr[mid] == x:
                index = mid
                low = mid+1
            elif arr[mid] < x:
                index = mid
                low = mid+1
            else:
                high = mid-1
        return index
                
            
            
arr = list(map(int,input().split()))
x = int(input())
sol =Solution()
print(sol.findFloor(arr,x))