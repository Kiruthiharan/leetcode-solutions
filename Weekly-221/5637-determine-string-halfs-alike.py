s = "book"

length = len(s)
half = length / 2
i = 0
count = 0
while(i < length):
    if(i < half):
        if(s[i].lower() in 'aeiou'):
            count +=1
    else:
        if(s[i].lower() in 'aeiou'):
            count -=1
    i += 1

print(True if count==0 else False)

# Optimised
vowels = set('aeiouAEIOU')
a = b = 0
i, j = 0, len(s) - 1
while i < j:
    a += s[i] in vowels
    b += s[j] in vowels
    i += 1
    j -= 1
print(a == b)