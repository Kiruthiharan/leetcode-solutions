nums = [1,4,6,8,10]
nms_iter = enumerate(nums)
result = []
matrix = ()
for i, i_index in nms_iter:
    temp = 0
    for j, j_index in nms_iter:
        if (matrix[i_index][j_index] != ''):
            break
        temp = temp + abs(i - j)
        matrix[i_index][j_index] = temp
        matrix[j_index][i_index] = temp
    result.append(temp)

print(result)
print(matrix)
