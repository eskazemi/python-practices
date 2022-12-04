#selection sort function

my_list = list(map(int,input().split()))
def selection_sort(my_list):
    """
        Args:
            my list type(list): 8 9 5 1 3 4 5 19 11 
        Raises:
            TypeError: my list isinstance list.
        Returns:
            list : [1 3 4 5 5 8 9 11 19] 
    """
    # find a minimum number is unsorted part of array
    for i in range(len(my_list)):
        minindex = i
        for j in range(i+1, len(my_list)):
            if my_list[minindex] > my_list[j]:
                minindex = j

        my_list[i], my_list[minindex] = my_list[minindex], my_list[i]

    # swap section is started at end of each round
    return my_list

print(selection_sort(my_list))