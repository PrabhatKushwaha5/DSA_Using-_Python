def rotateArray(nums,left,right,k):
    n = len(nums)
    while left < right:
        nums[left], nums[right] = nums[right],nums[left]
        left += 1
        right += 1

nums  = list(map(int,input().split()))
left = int(input())
right = int(input())
k = int(input())
rotateArray(n-k,n-1)
rotateArray(0,n-k-1)
rotateArray(0,n-1)
rotateArray(nums,left,right,k)
print(rotateArray)