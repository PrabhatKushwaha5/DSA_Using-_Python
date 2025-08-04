n = list(map(str,input().split()))
m = list(map(str,input().split()))
hash_list = [0]*26
for ch in n:
    ass_value = ord(ch)
    index = ass_value - 97
    hash_list[index] += 1

for ch in m:
    ass_value = ord(ch)
    index = ass_value - 97
    print(hash_list[index])