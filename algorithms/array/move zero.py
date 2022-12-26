def check_characters(character):
    if character.isnumeric():
        return int(character)
    elif character.capitalize() == 'True':
        return bool(character)
    elif character.capitalize() == 'False':
        return bool("")
    else:
        return character

input_user = list(map(check_characters, input().split()))

def zero(seq):
    """
    [False, 1, 3, 0, 5, 8, 'a', 0, 4, 'b'] -> [False, 1,3,5,8,'a',4,'b', 0, 0] 
    
    Args:
        seq(array)
    Raise:
        TypeError: seq is not instance of list
    Return:
        An array whose zeros are placed at the end of the list  
    """
    result=[]
    zeroes=0
    for i in seq:
        if i ==0 and type(i)!= bool:
            zeroes +=1
        else:
            result.append(i)

    result.extend([0] * zeroes)
    return result


print(zero(input_user))
