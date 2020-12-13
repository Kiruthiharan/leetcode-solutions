n = "32"

def split(word): 
    return [int(char) for char in word] 

nums = split(n)
print(max(nums))