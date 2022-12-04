my_array = list(map(int, input().split()))

def recursive_bubble_sort(my_array, is_sorted, step):
    """
        recursive bubble sort as a pyhton function
        Args:
            my_array(list)
        Raises:
            TypeError my array is not instance list
        Returns:
            sorted my list by recursive bubble_sort
    """
    if step == 1 or is_sorted:
        return my_array

    else:
        is_swapped = False
        for i in range(len(my_array)-1):
            if my_array[i] > my_array[i+1]:
                my_array[i] , my_array[i+1] = my_array[i+1] , my_array[i]
                is_swapped = True
        return recursive_bubble_sort(my_array, not is_swapped, step-1)


print(recursive_bubble_sort(my_array, False, step=len(my_array)))