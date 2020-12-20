nums = [4,2,4,5,6]
dict = {}


i = 0
j = 1

dict[nums[0]] = 1

sum = nums[0]
maxSum = sum

while(i < len(nums) -1 and j < len(nums)):
    if(nums[j] in dict):
        del dict[nums[i]]
        sum -= nums[i]
        i+=1
    else:
        sum += nums[j]
        maxSum = max(maxSum, sum)
        dict[nums[j]] = 1
        j+=1

print(maxSum)