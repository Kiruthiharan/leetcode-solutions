nums = [2,5,4,4,1,3,4,4,1,4,4,1,2,1,2,2,3,2,4,2]
k = 3

hash = {}
result = 0
for num in nums:
    if (num >= k):
        continue

    target = k-num
    if ( target in hash):
        result+=1
        hash[target]-=1
        if (hash[target] == 0):
            del hash[target]
    else:
        if ( num in hash):
            hash[num]+=1
        else:
            hash[num]=1


print(hash)
print(result)
