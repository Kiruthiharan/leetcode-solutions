s = "PAYPALISHIRING" 
numRows = 3
# not complete

inc = (numRows - 1) * 2
l = len(s)
res = []
i = 0
while(i < inc):
    j = i
    while(j < l):
        res.append(s[j])
        j += inc
    i += 1
    
print(res)
