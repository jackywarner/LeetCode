# Data structures utilized:
# 1. hashmap, hashmap = {} 
#   map keys to values (kinda like a dictionary) 
# 2. emumerate() 
#   takes an iterable object like list tuble or string and return an iterator that produces tubles containg the index containing the index and the value of each element 
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # dictionary/hashmap to store the indicies of the numbers 
        hash_table = {}
        # use enumerate() to create indexes 
        for i, num in enumerate(nums):
            # if the number we want in the hashtable is in our hashtable we return the indexes 
            if target - num in hash_table:
                return [i, hash_table[target-num]]
            # else we put that number in our hashtable and map it to the index it has 
            else:
                hash_table[num] = i
        #if it's none of the above just return an empty list 
        return []

        