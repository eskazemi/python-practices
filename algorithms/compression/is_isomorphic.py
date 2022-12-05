def is_isomorphic(s,t):
    """
    This function checks whether Are these two strings symmetrical with each other or not.
    Args:
        s(string)
        t(string)
    Raise:
        TypeError
    Return:
        bool
    """
    if len(s) != len(t):
        return False
    
    set_values=set()
    dict={}
    for i in range(len(s)):
        if s[i] not in dict:
            if t[i] in set_values:
                return False
            dict[s[i]]=t[i]
            set_values.add(t[i])
        else:
            if dict[s[i]] != t[i]:
                return False
    return True


