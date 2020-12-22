
# solution - sliding window
# speed - 22, memory - 97
# s = "1"

# if(len(s) == 0):
#     print(0)

# i = 0
# j = 1

# dict = {}
# dict[s[0]] = 1
# result = 1
# current = 1
# while( i != len(s)-1 and j != len(s)):
#     if(s[j] in dict.keys()):
#         if(s[i] in dict.keys()):
#             current -= 1
#             del dict[s[i]]
#             i += 1
#         else: 
#             j +=1
#     else: 
#         dict[s[j]] = 1
#         current += 1
#         result = max(result,current)
#         j += 1

# print(result)

# sliding window optimized
s = "abcabcbb"

i = 0
dict = {}
result = 0
for j in range(len(s)):
    if(s[j] in dict.keys()):
        i = max(dict[s[j]], i)
    result = max(result, j - i + 1)
    dict[s[j]] = j + 1

print(result)
