number = "--17-5 229 35-39475 "
number = number.replace(" ", "")
number = number.replace("-", "")

n = len(number)
result = ""
i = 0
while(n>1):
    if(n==4):
        result = result + "-" + number[i] + number[i+1] + "-" + number[i+2] + number [i+3]
        break
    elif(n==3):
        result = result + "-" + number[i] + number[i+1] + number[i+2]
        break
    elif(n==2):
        result = result + "-" + number[i] + number[i+1]
        break
    result = result + "-" + number[i] + number[i+1] + number[i+2]
    n-=3
    i+=3

print(result[1:])


