# Insertion Sort a python function 

my_list = list(map(int, input().split()))

def insertion_sort(my_list):
    """
        Insertion Sort a python function 

        Args:
            list (my_list): [50, 12 ,75 ,90, 36]
        Raises:
            TypeError: my list is not instance list
        Returns:
            list sorted
    """
    
    # Traverse through 1 to len(arr)
    for i in range(1, len(my_list)):
        temp = my_list[i]
        j = i-1
        while j >= 0 and temp < my_list[j]:
            my_list[j+1] = my_list[j]
            j -= 1

        my_list[j+1] = temp
    return my_list

print(insertion_sort(my_list))
