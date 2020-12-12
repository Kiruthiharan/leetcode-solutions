n=12

binaryNum = ''
modulo = 1000000007
for num in range(n,0,-1):
    binNum = bin(num)[2:]
    binaryNum = binNum + binaryNum

result = int(binaryNum, 2)
print(result % modulo)


