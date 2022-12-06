array = list(map(int, input().split()))


def bead_sort(array):
    """
    Args:
        array(list)
    Raise:
        TypeError: array must be list  of not-negative integers
    Return:
        list sorted
    """
    if any(not isinstance (x,int) or x <0 for x in array):
        return TypeError(' array must be list of not-negative integers')
    
    for _ in range(len(array)):
        for i,(rod_upper,rod_lower) in enumerate(zip(array,array[1:])):
            if rod_upper > rod_lower:
                array[i] -= rod_upper- rod_lower
                array[i+1] += rod_upper- rod_lower
    return array

print(bead_sort(array))