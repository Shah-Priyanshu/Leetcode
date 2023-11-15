class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        sum=0
        max_sum=nums[0]

        for num in nums:
            if sum+num>0:
                sum+=num
                if sum>max_sum:
                    max_sum=sum
            else:
                sum=0
                if num>max_sum:
                    max_sum=num

        return max_sum