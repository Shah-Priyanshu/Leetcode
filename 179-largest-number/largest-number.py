from functools import cmp_to_key

class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        # Convert the integers to strings since we will be comparing concatenated results
        nums_str = list(map(str, nums))
        
        # Custom comparator function
        def compare(x, y):
            if x + y > y + x:
                return -1
            elif x + y < y + x:
                return 1
            else:
                return 0
        
        # Sort the numbers based on the custom comparator
        nums_str.sort(key=cmp_to_key(compare))
        
        # Join the sorted strings
        largest_num = ''.join(nums_str)
        
        # Edge case: when the numbers are all zeros, we return "0" instead of "000..."
        return '0' if largest_num[0] == '0' else largest_num