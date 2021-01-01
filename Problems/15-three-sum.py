nums = [-1,0,1,0]

if(len(nums) < 3):
    print([])

dict = {}

for num in nums:
    dict[num] = dict.get(num, 0) + 1

result = set()
for index,i in enumerate(nums):
    for j in nums[index+1:]:
        if(i == j and dict[i] < 2):
            continue
        comp = -(i+j)
        if(comp in dict.keys()):
            if((i == j == comp and dict[i] < 3) or (i == comp and dict[i] < 2) or (j == comp and dict[j] < 2)):
                continue
            temp = [i,j,comp]
            temp.sort()
            result.add(tuple(temp))

print(result)