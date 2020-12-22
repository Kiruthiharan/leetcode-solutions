nums = [3,2,4]
target = 6

dict = {}
result = []
for index,num in enumerate(nums):
    complement = target - num
    if(complement in dict.keys()):
        result = [dict[complement], index]
        break
    else:
        dict[num] = index

print(result)