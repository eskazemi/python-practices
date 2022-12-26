
s = input("phrase: ")
k = int(input("rotates: "))

def rotate(s,k):
    """
    This function Given a strings s and int k, return a string that rotates k times
    For example,
        rotate("hello", 2) return "llohe"
        rotate("hello", 5) return "hello"
    ===========
    Args:
        s(string)
        k(int)
    Raise:
        TypeError
    Return:
        return a string that rotates k times

    """
    double_s=s+s
    if k <= len(s):
        return double_s[k:k+len(s)]
    else:
        return double_s[k-len(s):k]


print(rotate(s,k))