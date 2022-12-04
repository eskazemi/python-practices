my_array = list(map(int, input().split()))
item = int(input("The item you are looking for: "))


def binary_search(array, item_search, low, high):
    """
        binary search approach recursively 
        Args:
            array (my_list): [50, 12 ,75 ,90, 36]
            item_search (int)
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
    # To prevent overflow from the side h (l>h)
    # To prevent overflow from the side l (1=h)
    if low >= high:
        if array[low] == item_search:
            return f"This item found at index {low}"
        else:
            return "Not Found"

    else:
        mid = int((low + high) / 2)
        if array[mid] == item_search:
            return mid
        elif item_search < array[mid]:
            return binary_search(array, item_search, low, mid - 1)

        else:
            return binary_search(array, item_search, mid + 1, high)


print(binary_search(my_array, item, low=0, high=len(my_array) - 1))
