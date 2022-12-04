# input 
my_array = list(map(int, input().split()))


def partition(my_array, low, high):
    i = low - 1
    pivot = my_array[high]
    for j in range(low, high):
        if my_array[j] <= pivot:
            i +=1
            my_array[i], my_array[j] = my_array[j], my_array[i]
    my_array[i+1], my_array[high] = my_array[high], my_array[i+1]
    return i+1



def quick_sort(my_array, low, high):
    """
        Quick Sort a python function 

        Args:
            my_array (list): [50, 12 ,75 ,90, 36]
            low (int)
            high (int)
        Raises:
            TypeError: my array is not instance list
        Returns:
            list sorted
    """
    if low < high:
        index = partition (my_array, low, high)
        quick_sort(my_array, low, index-1)
        quick_sort(my_array, index, high)

    return my_array



print(quick_sort(my_array, low=0, high=len(my_array)-1))