my_list = list(map(int,input()))
def selection_sort(my_list):
    for i in range(len(my_list)):
        minindex = 0
        for j in range(i+1, len(my_list)):
            if my_list[minindex] > my_list[j]:
                minindex = j

        my_list[i], my_list[minindex] = my_list[minindex], my_list[i]

    return my_list