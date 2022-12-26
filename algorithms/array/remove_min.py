input_user = list(map(int, input().split()))

def remove_min(stack):
    """
    Args:
        stack(list)

    Raise:
        TypeError

    Return:
        input list without minimum value
    """
    result=[]
    if len(stack)==0:
        return stack

    min=stack.pop()
    stack.append(min)
    for i in range(len(stack)):
        val=stack.pop()
        if val <= min:
            min=val
        result.append(val)

    for i in range(len(result)):
        if result[i] != min:
            stack.append(result[i])
    return stack,min


print(remove_min(input_user))