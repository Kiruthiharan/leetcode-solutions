# not complete
s = "12"
x = 0
y = -1

x_val = ''
y_val = ''
temp = ''
length = len(s)
count = 0
flag = 0
while(x < length):
    if(s[x] != '0'):
        flag = 1
    if(y != -1):
        y_val = s[y]
        x_val = s[x]
        if(y_val == '0'):
            count -= 1
            x +=1
            y +=1
            continue
        temp = int(y_val + x_val)
        if(temp < 27):
            count += 1
        x +=1
        y +=1
    else:
        x += 1
        y = 0
        continue

if(flag ==1 ):
    count+=1
print(count)
