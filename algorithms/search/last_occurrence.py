
nums = list(map(int, input("nums: ").split()))
target=int(input("target: "))

def last_occurrence(nums,target):
    """
    Find last occurance of a number in a sorted array (increasing order)
    Approach- Binary Search
    T(n)- O(log n)
    Args:
        nums: List[int]
        target: int
    Raise:
        TypeError
    Return:
        Returns the index of the last occurance of the given element in an array.
    """
    low, high=0, len(nums)-1
    while low <= high:
        mid=low+(high-low)//2
        if (nums[mid] == target and mid==len(nums)-1) or \
            (nums[mid] == target and nums[mid+1]>target):
            return mid 
        elif (nums[mid] <= target):
             low=mid+1
        else:
            high=mid-1
           
    

print(last_occurrence(nums,target))