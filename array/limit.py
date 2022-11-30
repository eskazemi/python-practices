
def limit(arr,min=None,max=None):
    """
        Args:
            arr (array):[1,2,3,4,5]
            min (int): 3
            max (int): 3
        Raises:
            TypeError: if min and max not instance of int
            TypeError: if arr not instance of array
        Returns:
           array
    """
    min_check=lambda val: True if min is None else (val >= min)
    max_check=lambda val: True if max is None else (val <= max)

    return[val for val in arr if min_check(val) and max_check(val)]

print(limit([1,2,3,4,5,6,7],max=6))
