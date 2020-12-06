command = "(al)G(al)()()G"

o_Flag = False
al_Flag = False

result = ""

for item in command:
    if item == 'G':
        result += "G"
    elif item == '(':
        o_Flag = True
        al_Flag = True
    elif item == 'a':
        o_Flag = False
    elif item == ')':
        if o_Flag:
            result += "o"
            o_Flag = False
        elif al_Flag:
            result += "al"
            al_Flag = False
print (result)