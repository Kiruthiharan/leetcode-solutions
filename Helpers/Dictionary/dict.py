nums = [-1,0,1,2,-1,-4]

# Add count to dict
dict = {}
for num in nums:
    dict[num] = dict.get(num, 0) + 1

# Add indexes to dict
for i, x in enumerate(nums):
    dict.setdefault(x, []).append(i)