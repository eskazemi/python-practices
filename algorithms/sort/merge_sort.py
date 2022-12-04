
my_array = list(map(int, input().split()))

def merge_sort(my_array):

    """
        merge Sort a python function 
        Args:
            list (my_list): [50, 12 ,75 ,90, 36]
        Raises:
            TypeError: my list is not instance list
        Returns:
            list sorted
    """
    if len(my_array) > 1:
        mid = int(len(my_array) / 2)
        L = my_array[:mid]
        R = my_array[mid:]
        merge_sort(L)
        merge_sort(R)
        i=j=k = 0
        # merge function
        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                my_array[k] = L[i]
                i +=1
            else:
                my_array[k] = R[j]
                j += 1
            k += 1

        while i < len(L):
            my_array[k] = L[i]
            i += 1
            k += 1
        
        while j < len(R):
            my_array[k] = R[j]
            j += 1
            k += 1

    
    return my_array


print(merge_sort(my_array))
# for a in my_array:
#     print(a, end="")