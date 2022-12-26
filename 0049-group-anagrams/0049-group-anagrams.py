# Data structure used
# 1. '' 
#   '' is jsut an empty string. so ''.join(["t","e","a"]) would be "tea"
# 2. join
#   A function that concatenaes all the characters into a single string 
# 3. sorted()
#   Python sort function. It will return a list of characters so if we wanted to sort "eat" it would become ['a','e','t']

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        hashmap = {}
        # Go through every word in strs
        for word in strs:
            # resort each word in the list to be alphabetical
            key = ''.join(sorted(word))
            # see if the key already exists in the hashmap
            if key in hashmap:
                # will look like {aet : tea}
                hashmap[key].append(word)
            # else append a new key with the word 
            else:
                hashmap[key] = [word]
        # return the whole list     
        return list(hashmap.values())