# You are given an array people where people[i] is the weight of the ith person, and an infinite number of boats where each boat can carry a maximum weight of limit. Each boat carries at most two people at the same time, provided the sum of the weight of those people is at most limit.

# Return the minimum number of boats to carry every given person.

 

# Example 1:

# Input: people = [1,2], limit = 3
# Output: 1
# Explanation: 1 boat (1, 2)
# Example 2:

# Input: people = [3,2,2,1], limit = 3
# Output: 3
# Explanation: 3 boats (1, 2), (2) and (3)
# Example 3:

# Input: people = [3,5,3,4], limit = 5
# Output: 4
# Explanation: 4 boats (3), (3), (4), (5)

class Solution:
    def numRescueBoats(self, people, limit):
        people.sort()
        res = 0 # boats
        l, r = 0, len(people) - 1 
        
        while l <= r:
            remain = limit - people[r]
            r -= 1 
            res += 1 
            if l <= r and remain >= people[l]:
                l += 1 
        
        return res 
    

class Solution(object):
    def numRescueBoats(self, people, limit):
        """
        :type people: List[int]
        :type limit: int
        :rtype: int
        """
        people.sort()
        l, r = 0, len(people) - 1 
        res = 0
        
        while l <= r:
            if people[r] + people[l] <= limit:
                r -= 1 
                l += 1
            else:
                r -= 1 
            res += 1 
        
        return res    