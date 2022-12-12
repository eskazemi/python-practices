
nums = list(map(int, input("nums: ").split()))
target = int(input("target: "))
def first_occurrence (nums,target):
    """
    Find first occurance of a number in a sorted array (increasing order)
    Approach- Binary Search
    T(n)- O(log n)
    Args:
        nums: List[int]
        target: int
    Raise:
        TypeError
    Return:
         Returns the index of the first occurance of the given element in an array. 
    """
    low, high =0 ,len(nums)-1
    while low <= high:
        print(low)
        print(high)
        if low==high:
            break
        mid=low+(high-low)//2
        val=nums[mid]

        if val < target:
            low=mid+1
        else:
            high=mid

    if nums[low]==target:
        return low

    

print(first_occurrence(nums,target))