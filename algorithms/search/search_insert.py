def search_insert(array,val):
    """
    Given a sorted array and a target value, return the index if the target is
    found. If not, return the index where it would be if it were inserted in order.
    For example:
    [1,3,5,7], 5 -> 2
    [1,3,5,9], 2 -> 1
    [1,3,5,6], 7 -> 4
    [1,3,5,6], 0 -> 0
    Args:
        list (array): [2,4,5,7,8]
        val (int)
    Raises:
        TypeError: array is not instance list
        TypeError: val is not int
    Returns:
            index val
    """
    low=0
    high=len(array)-1
    mid=high//2

    while low <= high:
        if val > array[mid]:
            mid +=1
            low=mid
        else:
            mid -=1
            high=mid
    return low


def main():
    array = list(map(int, input("array: ").split(" ")))
    value = int(input("value: "))
    print(search_insert(array, value))


main()