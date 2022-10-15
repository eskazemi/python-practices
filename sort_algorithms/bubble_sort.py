from time import time


my_array = list(map(int, input().split()))


def bubble_sort(my_array):
    """
        bubble sort as a pyhton function
        Args:
            my_array(list)
        Raises:
            TypeError my array is not instance list
        Returns:
            sorted my list by bubble_sort
    """
    for i in range(len(my_array)):
        for j in range(0, len(my_array)-i-1):
            if my_array[j] > my_array[j+1]:
                my_array[j] , my_array[j+1] = my_array[j+1] , my_array[j]

    return my_array

# print(bubble_sort(my_array))


def optimized_bubble_sort(my_array):
    """
        bubble sort as a pyhton function
        Args:
            my_array(list)
        Raises:
            TypeError my array is not instance list
        Returns:
            sorted my list by bubble_sort
    """
    is_swapped = False
    for i in range(len(my_array)):
        for j in range(0, len(my_array)-i-1):
            if my_array[j] > my_array[j+1]:
                my_array[j] , my_array[j+1] = my_array[j+1] , my_array[j]
                is_swapped = True
        if is_swapped == False:
            break

    return my_array


print(optimized_bubble_sort(my_array))
