allowed = "cad"
words = ["cc","acd","b","ba","bac","bad","ac","d"]
def split(word): 
    return [char for char in word] 

chars = split(allowed)

count = 0
for word in words:
    flag = 0
    for item in word:
        if (item not in chars):
            flag = 1
            break
    if (flag == 0):
        count +=1

print(count)