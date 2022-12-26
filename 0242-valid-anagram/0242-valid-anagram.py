# Data structures utilized:
# 1. frequency map f_map = {}
#   A dictionary that stores the frequency of each character in a string. 
#
# 2. code point
#   numerical value that represnts a character in a character encoding system ASCII or Unicode. Each character is assigned a unique code point. A is 65, B is 66, etc. 
# 3. ord()
#   this get the unicode point for each character 
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # create a frequency map for both s and t
        s_frequency_map = {}
        t_frequency_map = {}
        # iterate through s string 
        for char in s:
            # create a code_point based on each character since we are dealing with Unicode characters 
            code_point = ord(char)
            #look for the code_point in the frequency map if it's in side add one should look like:
            # *for example if it's letter 'A'
            # {'a' : 1}
            if code_point in s_frequency_map: 
                s_frequency_map[code_point] += 1 
            #else add a freuqncy map of the value and set it to 1 
            else:
                s_frequency_map[code_point] = 1
        # do the same for the string t 
        for char in t:
            code_point = ord(char)
            if code_point in  t_frequency_map:
                t_frequency_map[code_point] += 1
            else:
                t_frequency_map[code_point] = 1
        #compare the two frequency maps to see if they are the same 
        return s_frequency_map == t_frequency_map 
            
            
            
            
            
            
            
            