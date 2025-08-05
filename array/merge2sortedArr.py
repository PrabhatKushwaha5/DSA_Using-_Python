def mergeTwoSortedArray(nums1,nums2):
    m = len(nums1)
    n = len(nums2)
    result = []
    i,j=0,0
    while i<m and j<n:
        if nums1[i] <= nums2[j]:
            if len(result) == 0 or result[-1] != nums1[i]:
                result.append(nums1[i])
            i += 1
        else:
            if len(result) == 0 or  result[-1] != nums2[j]:
                result.append(nums2[j])
            j +=1
    while i<m:
        if len(result) == 0 or  result[-1] != nums1[i]:
            result.append(nums1[i])
        i += 1
    while j<n:
        if len(result) == 0 or  result[-1] != nums2[j]:
            result.append(nums2[j])
        j +=1
    return result

nums1 = list(map(int,input().split()))
nums2 = list(map(int,input().split()))
merged_arr = mergeTwoSortedArray(nums1,nums2)
print(merged_arr)
