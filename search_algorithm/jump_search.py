my_array = list(map(int, input().split()))
item = int(input("item search: "))


import math

def jump_search(my_array, item, n):
    """
        jump search a python function 
        Args:
            list (my_array)
            item (int) : item serach
            n (int): length array
        Raises:
            TypeError: my array is not instance list
            TypeError: item is not int
            TypeError: n is not int
        Returns:
            index item or not found
    """
    # Finding block size to be jumped
    jump_length = math.sqrt(n)
    prevstep = 0

    while my_array[int(min(jump_length, n)-1)] < item:
        prevstep = jump_length
        jump_length += math.sqrt(n) 

        if prevstep >= n:
            return -1

    # Doing a linear search for x in
    # block beginning with prev.
    while my_array[int(prevstep)] < item:
        prevstep +=1

        # If we reached next block or end
        # of array, element is not present.
        if prevstep == min(jump_length,n):
            return -1

    if my_array[int(prevstep)] == item:
        return int(prevstep)

    else:
        return -1


# Find the index of 'x' using Jump Search
index = (jump_search(my_array, item, len(my_array)))
 
# Print the index where 'x' is located
if index != -1:
    print("Number" , item, "is at index" , index)
else:
    print("Not found")