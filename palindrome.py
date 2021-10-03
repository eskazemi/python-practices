#palindrome : A phrase that reads the same from beginning to end.
#example level
#* if a character or تهی , is palindrome

def palindrome(s):
    if len(s) <= 1:
        return True
    
    else:
        if s[0] == s[len(s)-1]:
            return palindrome(s[1:len(s)-1])
        else:
            return False

print(palindrome('age'))