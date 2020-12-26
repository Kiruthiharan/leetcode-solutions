students = [1,1,0,0]
sandwiches = [0,1,0,1]

i = 0 #sandwiches
j = 0 #students
count = 0
while(count != (len(sandwiches) - i)):
    if(sandwiches[i] == students[j]):
        i += 1
        j += 1
        count = 0
    else:
        students.append(students[j])
        j += 1
        count += 1

print(len(sandwiches) - i)