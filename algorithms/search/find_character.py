#find_character
def find_char(s,ch):
    x = 0 
    while x < len(s):
        if s[x] == ch:
            return x
        x +=1

    return -1 # is not exists


def find_character(s,ch,start=0, end=0):
    i = start
    if end is None:
        end = len(s)

    while i < end:
        if s[i] == ch:
            return i

        i +=1

    return -1

print(find_character("Automation", "t", 0 , None))


print(find_char("Automation", "t"))