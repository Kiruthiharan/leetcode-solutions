S = "leet2code3" 
K = 10

result = ""
flag = None
total = 0
for val in S:
    if(val.isalpha()):
        flag = 0
    elif(val.isdigit()):
        n = int(val) - 1
        total +=n
    if(flag == 0):
        result = result * total
        result += val
        flag = 1
        

print(result)