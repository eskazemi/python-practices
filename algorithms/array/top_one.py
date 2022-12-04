
def top(array: list):
    """
    This algorithm gets an array, makes a dictionary of it finds the most 
    frequent count, and makes the result list
    Args:
        array (list)
    Raises:
        TypeError: array not instance list
    Returns:
        array
    """
    values={}
    result=[]
    f_val=0
    for i in array:
        if i in values:
            values[i] +=1
        else:
            values[i]=1
    f_val=max(values.values())
    
    for i in values.keys():
        if values[i]==f_val:
            result.append(i)
        else:
            continue
    return result

