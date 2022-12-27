# Data Structures utilized
# 1. sorted() 
#   1st arguement would be the hashmap, it will sort the hashmap, 
#   2nd arguement would be the key parameter which is a funciton that takes an elemnt as input and returns the corresponding values in the 'frequency_count' dictionary. So instead of sorting based on the the key, it will now sort based on the frequency. 
#   3rd arguement would be reverse, sort it in descending order, largest to lowest, in this case
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Dictionary to store the count 
        hashmap = {} 
        # This should create a dictionary of each number and how many occurance there are
        # i.e. [1,1,1,2,2,3] -> {1:3, 2:2, 3:1}
        for num in nums: 
            if num in hashmap:
                hashmap[num] += 1
            else:
                hashmap[num] = 1
        
        # We want the alogrithm's time complexity to be better than O(n log n), where n is the array's size
        #we knwo the time complexity of sorted() is O(N log N)
        sorted_elements = sorted(hashmap, key=hashmap.get, reverse=True)
        
        # this will return the top k elements. 
        return sorted_elements[:k]