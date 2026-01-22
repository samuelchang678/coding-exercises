from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)-1):
            for j in range(i+1, len(nums)):
                randomSum = nums[i] + nums[j] 
                if(randomSum == target):
                    return [i,j]
        


if __name__ == "__main__":
    solution = Solution()
    print(solution.twoSum([2, 7, 11, 15], 9))
    print(solution.twoSum([3,2,4], 6))
    print(solution.twoSum([3,3], 6))



'''
    My solution would be considered naive, O(N^2) cause of the 2 for loops

    The optimal way to do it would be the following

    1. create an empty dictionary (seen)
    2. Then enumerate through the list, enumerate([2,7,11,15]) gets you [(0, 2), (1, 7), (2, 11), (3, 15)]
    3. Deduct the number from target and we want to check if remainder is in the dictionary
    4. If remainder if in dictionary then return the index of remainder with i(current index);
    5. If not insert (number(key), index(value)) pair into the dictionary

    What is unique is that this solution uses the number as the key instead of index,... i mean if index is key then its an array....

    Also this has an O(N) search with space (N), we only need to loop the List once. 

    *Dictionary search is O(1) on average so we can ignore that. 
'''

class bestSolution:

    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {} # Empty dictionary
        

        for i, num in enumerate(nums):
            remainder = target - num
            if remainder in seen: 
                return [seen[remainder],i]
            seen[num] = i