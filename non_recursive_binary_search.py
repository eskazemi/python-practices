my_array = list(map(int, input().split()))
item = int(input("The item you are looking for: "))

def binary_search(my_array, item):
    """
        binary search non recursive
        Args:
            list (my_list): [50, 12 ,75 ,90, 36]
            item (int)
        Raises:
            TypeError: my list is not instance list
            TypeError: item is not int
        Returns:
            index item or not found
    """
    high = len(my_array)-1
    low = 0
    
    while(low <= high):
        mid = int((low + high)/2)
        if my_array[mid] == item:
            return f"This item found at index {mid}"

        elif item < my_array[mid]:
            high = mid -1
    
        else:
            low = mid + 1

    return "Not Found"



print(binary_search(my_array, item))