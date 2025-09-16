"""in this code we have two list 
we fetch one list and store the 
frequrncy in the hash_list
and after that we fetch the another list and check the 
number present in hash_list and print that number frequency"""

n = list(map(int,input().split()))
m = list(map(int,input().split()))
hash_list = [0]*11 #because in list one only 1 to 10 number present
for i in n:
    hash_list[i] += 1
    

for j in m:
    if j < 1 or j > 10:
        print(0)
    else:
        print(hash_list[j])
