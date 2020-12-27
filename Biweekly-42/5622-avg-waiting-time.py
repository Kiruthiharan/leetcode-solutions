customers = [[5,2],[5,4],[10,3],[20,1]]
# wrong 
i = 0
length = len(customers)
total = 0
total_waiting = 0
while(i < length):
    if(i == 0):
        total +=customers[i][0] + customers[i][1]
        total_waiting += customers[i][1]
        i += 1
        continue
    if(customers[i][0] > total):
        total = customers[i][0]
        total_waiting += customers[i][1]
        i += 1
        continue
    total += customers[i][1]
    total_waiting += total - customers[i][0]
    i += 1

print(float(total_waiting) / length)