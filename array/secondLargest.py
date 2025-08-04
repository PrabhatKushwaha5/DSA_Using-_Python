def secondLargest(arr):
	# code here
	largest = float("-inf")
	s_largest = float("-inf")
	n = len(arr)
		
	for i in range(0, n):
		largest = max(largest, arr[i])
		    
	for i in range(0, n):
		if arr[i] != largest and arr[i] > s_largest:
			s_largest = arr[i]
		
	if s_largest == float("-inf"):
		return -1  

	return s_largest

arr = list(map(int, input().split()))
print(secondLargest(arr))
