
my_array = list(map(int, input().split()))


def recursive_insertion_sort(my_array, n):
    """
        Args:
            my_array(list)
            n(int): len(my_array)
        Raises:
            TypeError my array is not instance list
        Returns:
            sorted my list by recursive insertion sort
    """
    if n == 1:
        return

    recursive_insertion_sort(my_array, n-1)
    temp = my_array[n-1] # (50 index 0, 74 index 1)
    j = n-2
    while j >= 0 and my_array[j] > temp:
        my_array[j+1] = my_array[j]
        j -=1

    my_array[j+1]= temp

    return my_array

print(recursive_insertion_sort(my_array, len(my_array)))
