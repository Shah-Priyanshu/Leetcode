class Solution(object):
    def longestConsecutive(self, nums):
        nums = sorted(set(nums))
        
        if len(nums) == 0:
            return 0
        
        seq_lens = cur_len = 1
        for i,n in enumerate(nums[:-1]):
            if nums[i+1]-1 == n:
                cur_len += 1
            else:
                if cur_len > seq_lens:
                    seq_lens = cur_len
                cur_len = 1
        
        return max(cur_len,seq_lens)
