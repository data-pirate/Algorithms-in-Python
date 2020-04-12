def closest_pair(nums, target):
    min_diff = float('inf')
    closest_num = None
    if len(nums) == 0:
        return None
    if len(nums) == 1:
        return nums[0]
    
    low = 0
    high = len(nums)-1
    while low <= high:
        mid = (low + high) // 2

        # Ensure you do not read beyond the bounds
        # of the list.
        if mid+1 < len(nums):
            min_diff_right = abs(nums[mid+1]-target)

        if mid > 0:
            min_diff_left = abs(nums[mid-1]-target)
        
        
        # Check if the absolute value between left
        # and right elements are smaller than any
        # seen prior.
        if min_diff_left < min_diff:
            min_diff = min_diff_left
            closest_num = nums[mid-1]

        if min_diff_right < min_diff:
            min_diff = min_diff_right
            closest_num = nums[mid+1]

        # Move the mid-point appropriately as is done
        # via binary search.
        if nums[mid] < target:
            low = mid+1
        elif nums[mid] > target:
            high = mid-1

        # If the element itself is the target, the closest
        # number to it is itself. Return the number.
        else:
            return nums[mid]
    return closest_num

A1 = [1, 2, 4, 5, 6, 6, 8, 9]
print(closest_pair(A1, 7.4))
