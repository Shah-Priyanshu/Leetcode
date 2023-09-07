class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        #Create a dictionary to store the values and their indices
        num_dict = {}
        
        for i, num in enumerate(nums):
            complement = target - num
            
            # Check if the complement exists in the dictionary
            if complement in num_dict:
                return [num_dict[complement], i]
            
            # If not, add the current number and its index to 
            #the   dictionary
            num_dict[num] = i
        
        # If no solution is found, return an empty list or 
        #raise an exception
        return []        
        