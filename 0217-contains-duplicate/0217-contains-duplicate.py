# Data structures utilized:  
# 1. set()
#   unordered collection of unique elements. uused to store multiple items in a single object, can be used to perform operations such as membership testing, intersection, union, and difference. 
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        # Create a set to store unique values in
        unique_value_set = set() 
        # Iterate through each num in nums 
        for num in nums:
            # If the number is in the set, return true 
            if num in unique_value_set:
                return True
            # If the num is not in the set, add the num 
            else:
                unique_value_set.add(num)
        # If it finishes iterating through the set, then there is no duplicate
        return False
        