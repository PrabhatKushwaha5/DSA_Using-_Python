def merge_array(left,right):
    result = []
    n = len(left)
    m = len(right)
    i,j = 0,0
    while i<n and j < m:
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j+=1
    while i < n :
            result.append(left[i])
            i+=1
    while j < m:
            result.append(right[j])
            j+=1
    return result


def merge_sort(arr):
    if len(arr)<=1:
        return arr
    mid = len(arr)//2
    left_arr = arr[:mid]
    right_arr = arr[mid:]
    left = merge_sort(left_arr)
    right = merge_sort(right_arr)
    return merge_array(left,right)




arr = list(map(int,input().split()))
sorted_arr = merge_sort(arr)
print(sorted_arr)




"""
if len(arr) <= 1:
            return arr
        mid = len(arr)//2
        l = arr[:mid]
        r = arr[mid:]
        left = self.mergeSort(l,len(l),len(r))
        right = self.mergeSort(r,len(l),len(r))
        return self.mergeArray(left,right)
        
    def mergeArray(self,left,right):
        result = []
        i,j = 0,0
        m = len(left)
        n = len(right)
        
        while i < m and j < n:
            if left[i] <= right[j]:
                result.append(left[i])
                i+=1
            else:
                result.append(right[j])
                j+=1 
        while i < m:
            result.append(left[i])
            i += 1
        while j < n:
            result.append(right[j])
            j += 1
        return result
"""