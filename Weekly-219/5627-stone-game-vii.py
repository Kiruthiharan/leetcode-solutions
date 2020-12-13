stones = [5,3,1,4,2]

total = sum(stones)

alice = 1
bob = 0
temp = 0
result = 0
while (stones != []):
    if (len(stones) <= 2):
        if (stones[0] >= stones[-1]):
            temp = stones.pop(-1)
        else:
            temp = stones.pop(0)
        if (alice):
            total = total - temp
            result += total
            alice = 0
            bob = 1
        else:
            total = total - temp
            result -= total
            alice = 1
            bob = 0
        continue
    if (alice):
        if (stones[0] >= stones[-1]):
            temp = stones.pop(-1)
        else:
            temp = stones.pop(0)
        total = total - temp
        result += total
        alice = 0
        bob = 1
    else:
        op1 = min(stones[1], stones[-1])
        op2 = min(stones[0],stones[-2])
        if (op1 > op2):
            temp = stones.pop(0)
        else:
            temp = stones.pop(-1)
        total = total - temp
        result -= total
        bob = 0
        alice = 1
    print(total)

print(result)