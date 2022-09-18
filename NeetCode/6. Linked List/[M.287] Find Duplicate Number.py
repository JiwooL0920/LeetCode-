# Given an array of integers nums containing n + 1 integers where each integer is in the range [1, n] inclusive.

# There is only one repeated number in nums, return this repeated number.

# You must solve the problem without modifying the array nums and uses only constant extra space.

 
# Input: nums = [1,3,4,2,2]
# Output: 2

# Input: nums = [3,1,3,4,2]
# Output: 3
 
def findDuplicate(self, nums):
    slow, fast = 0, 0 
    
    # find first intersection 
    while True: 
        slow = nums[slow]
        fast = nums[nums[fast]]
        if slow == fast: 
            break 
        
    slow2 = 0 
    while True: 
        slow = nums[slow]
        slow2 = nums[slow2]
        if slow == slow2: 
            return slow 
        
        