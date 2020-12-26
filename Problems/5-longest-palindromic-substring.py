def checkPalindrome(arr):
    i = 0
    j = len(arr) - 1
    while(i<=j):
        if(arr[i] != arr[j]):
            return False
        i += 1
        j -= 1
    return True

s = "babad"
i = 0
j = 0
n = len(s)
max = 0
current = 0
final = ''
while(j < n):
    if(checkPalindrome(s[i:j+1])):
        current = j -i +1
        if(current > max):
            max = current
            final = s[i: j+1]
    j+=1
