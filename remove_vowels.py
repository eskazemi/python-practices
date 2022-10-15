#remove_vowels

def remove_vowels(s):
    vowels = "aeiou.AEIOU"
    t = ""
    for ch in s:
        if ch not in vowels:
            t +=ch
    return text


pritn(remove_vowels("Authentication"))
