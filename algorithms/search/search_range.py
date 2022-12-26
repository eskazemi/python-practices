
nums = list(map(int, input("nums: ").split()))
target = int(input("target: "))

def search_range (nums,target):
    """
    Given an array of integers nums sorted in ascending order, find the starting
    and ending position of a given target value. If the target is not found in the
    array, return [-1, -1].
    For example:
    Input: nums = [5,7,7,8,8,8,10], target = 8
    Output: [3,5]
    Input: nums = [5,7,7,8,8,8,10], target = 11
    Output: [-1,-1]
    Args:
        ums:List[int]
        target: int
    Raise:
        TypeError
    Return:
        return List[int]

    """
    low = 0
    high = len(nums) - 1
    while low <= high:
        mid = low+(high-low)//2
        if target < nums[mid]:
            high = mid-1
        elif target > nums[mid]:
            low=mid+1
        else:
            break
        
    for j in range(len(nums)-1,-1,-1):
        if nums[j] == target:
            return [mid ,j]
    
    return[-1,-1]


print(search_range(nums,target))