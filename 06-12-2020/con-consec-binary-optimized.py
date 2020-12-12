n=82679

modulo = 1000000007
answer = 0
pow = 1
while(n > 0):
    bin = n
    while (bin > 0):
        if (bin & 1):
            answer+=pow
        bin = bin >> 1
        pow = pow * 2
    n -= 1

print (answer % modulo)



