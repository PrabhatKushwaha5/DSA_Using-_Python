def selection_sort(nums):
    n = len(nums)
    for i in range(0,n):
        min_indx = i 
        for j in range(i+1,n):
            if nums[j] < nums[min_indx]:
                min_indx = j
        nums[i],nums[min_indx] = nums[min_indx],nums[i]

nums = list(map(int,input().split()))
selection_sort(nums)
print(nums)