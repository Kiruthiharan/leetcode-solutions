nums1 = [2]
nums2 = []

i = 0
j = 0

result = []
ans = 0
x = 0
y = 0
med_pos = int((len(nums1) + len(nums2)) / 2) + 1
print(med_pos)
while(len(result) <= med_pos):
    if( i < len(nums1)):
        x = nums1[i]
    else:
        x = 10000000

    if( j < len(nums2)):
        y = nums2[j]
    else:
        y = 10000000
    if(x < y):
        result.append(x)
        i += 1
    else:
        result.append(y)
        j +=1

print(result)
if((len(nums1) + len(nums2)) % 2 != 0):
    print(result[med_pos - 1])
else:
    print(float((result[med_pos-2] + result[med_pos-1])) / 2)



