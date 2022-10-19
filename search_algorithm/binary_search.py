my_array = list(map(int, input().split()))
item = int(input("The item you are looking for: "))

def binary_search(my_array, item, low, high):
    """
        binary search approach recursively 
        Args:
            list (my_list): [50, 12 ,75 ,90, 36]
            item (int)
            low (int)
            high(int)
        Raises:
            TypeError: my list is not instance list
            TypeError: item is not int
            TypeError: low is not int
            TypeError: high is not int
        Returns:
            index item or not found
    """
    #To prevent overflow from the side h (l>h)
    #To prevent overflow from the side l (1=h)
    if low >= high:
        if my_array[low] == item:
            return f"This item found at index {low}"
        else:
            return "Not Found"

    else:
        mid = int((low+high) / 2)
        if my_array[mid] == item:
            return mid
        elif item < my_array[mid]:
            return binary_search(my_array, item, low, mid-1)

        else:
            return binary_search(my_array, item, mid+1, high)

    


print(binary_search(my_array, item, low=0, high=len(my_array)-1))