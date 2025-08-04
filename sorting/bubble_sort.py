#average bubble sort
def bubble_sort(arr):
    n = len(arr)
    for i in range(n-2,-1,-1):
        for j in range(0,i+1):
            if arr[j]>arr[j+1]:
                arr[j],arr[j+1]=arr[j+1],arr[j]

    
arr = list(map(int,input().split()))
bubble_sort(arr)
print(arr)