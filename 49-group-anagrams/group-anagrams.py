class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        mp = defaultdict(list)
        for str in strs:
            sortedStr = "".join(sorted(str))
            mp[sortedStr].append(str)
        return list(mp.values())
        