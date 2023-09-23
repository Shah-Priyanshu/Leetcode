class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        d = {}
        for item in nums:
            if item in d:
                d[item] += 1
            else:
                d[item] = 1
        sorted_dict = sorted(d.items(), key=lambda x:x[1], reverse=True)
        l = []
        for key in sorted_dict:
            if k > 0:
                l.append(key[0])
                k -= 1
        return l