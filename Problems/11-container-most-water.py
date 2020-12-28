height = [1,8,6,2,5,4,8,3,7]
# two pointer approach
# i -->   <--j

i = 0
j = len(height) - 1

maxArea = 0
while(i < j):
    maxArea = max(maxArea, min(height[i], height[j]) * (j-i))
    if(height[i] < height[j]):
        i += 1
    else:
        j -=1

print(maxArea)

    
