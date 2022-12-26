numbers = list(map(int, input("array: ").split()))
target = int(input("target: "))

def two_sum(numbers,target):
    """
    Args:
        numbers(array)
        target(int)
    Raise:
        TypeError
    
    Return:
        [index, index] --> The sum of two numbers is the target number
    """
    p1=0
    p2=len(numbers)-1
    while p1 <p2:
        s=numbers[p1]+numbers[p2]
        if s ==target :
            return [p1,p2]
        if s >target:
            p2 -=1
        else:
            p1 +=1

print(two_sum(numbers,target))