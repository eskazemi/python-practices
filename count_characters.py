#count_characters
def count_char(text, ch):
    counter = 0
    for c in text:
        if c ==ch:
            counter +=1

    return counter


print(count_char("mehran", "m"))