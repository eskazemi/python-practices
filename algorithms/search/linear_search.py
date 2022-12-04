my_array = list(map(int, input().split()))
item = int(input("The item you are looking for:"))

def leaner_search(my_array, item):
    """
        leaner search a python function 
        Args:
            list (my_list): [50, 12 ,75 ,90, 36]
            item (int)
        Raises:
            TypeError: my list is not instance list
            TypeError: item is not int
        Returns:
            index item or not found
    """
    n = len(my_array)
    for i in range(0,n):
        if my_array[i] == item:
            return f"This index item is {i}"
    
    return ("This item is not in list")


print(leaner_search(my_array, item))