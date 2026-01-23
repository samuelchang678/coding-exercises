class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        longestStart = 0
        longestStop  = 0
        currentStart = 0
        currentStop = 0


        # while stop < len(s):
        valid = {}
        for i, letter in enumerate(s):

            if letter in valid:
                if (currentStop - currentStart > longestStop-longestStart):
                    longestStart = currentStart #override the longest substring length
                    longestStop= currentStop #override the longest substring length
                currentStart = i + 1
                valid.clear()
                continue #move on to the next index and 
            else: 
                valid[letter] = i # insert (letter(key), index(value)) into dictionary
                currentStop = i

        return longestStop-longestStart + 1
'''
    https://leetcode.com/problems/longest-substring-without-repeating-characters/description/

    Thoughts:
        - enumerate a string yes
        - need to loop
        - keep track of longest and start. and also length

    Things i did right:
    1. Use a dictionary, with correct key value pair
    2. Know the best approach was to be 1 loop and not 2 for loops.
    3. knew to keep track of an start index and longest length 

    mistakes :
    1. cleared dictionary. I am suppose to use the dictionary to track the index , not only its occurrence
    2. only update the "longest" when you find a duplicate (misses the end of string)
    3.Actually, no point keeping track of the longestStop, cause the current longest stop is always i
    and if you try to set it to any other value, then it would be wrong

    Solution: 
    1. When we meet a duplicate, then we move the longestStart to the index + 1.
    2. Do not need to clear dictionary, use it to store the index and use the index + 1 
    3. The right to do it is to compare the length (i - longestStart) at every iteration to the longestLength.
    
'''

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        longestStart = 0
        longestStop  = 0

        longestLength = 0 


        # while stop < len(s):
        valid = {}
        for i, letter in enumerate(s):
            if letter in valid and valid[letter] >= longestStart:
                # Move start to right after the previous occurrence
                longestStart = valid[letter] + 1
            valid[letter] = i

            contender = i - longestStart + 1
            if (contender >= longestLength):
                longestLength = contender
        return longestLength


    def lengthOfLongestSubstring(self, s: str) -> int:
        longestStart = 0
        longestStop  = 0

        longestLength = 0 


        # while stop < len(s):
        valid = {}
        for i, letter in enumerate(s):
            if letter in valid and valid[letter] >= longestStart:
                # Move start to right after the previous occurrence
                longestStart = valid[letter] + 1
                longestStop = valid[letter]+1
            else :
                longestStop = i 
            valid[letter] = i
            

            # contender = i - longestStart + 1
            # if (contender >= longestLength):
            #     longestLength = contender
        return longestStop - longestStart + 1



