class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        if (len(nums) < 4):
            return []
        
        nums.sort()
        min_sum = nums[0]+nums[1]+nums[2]+nums[3]
        max_sum = nums[-1]+nums[-2]+nums[-3]+nums[-4]

        if target < min_sum or target > max_sum:
            return []
        
        res = []
        num_map = {}
        num_list = []
        sum_map = {}
        for n in nums:
            if n not in num_map:
                num_map[n] = 1
                num_list.append(n)
            else:
                num_map[n] += 1
        
        for i in range(len(num_list)):
            for j in range(i, len(num_list)):
                n = num_list[i]
                m = num_list[j]
                if n != m or num_map[n] >= 2:
                    s = m + n
                    if s not in sum_map:
                        sum_map[s] = []
                    sum_map[s].append((n, m))
        
        for k in sum_map.keys():
            d = target - k

            if d in sum_map and k < d:
                for x, y in sum_map[k]:
                    for m, l in sum_map[d]:
                        if x == y and y == m and m < l and num_map[x] >= 3:
                            res.append([x, x, x, l])
                        elif x < y and y == m and m == l and num_map[l] >= 3:
                            res.append([x, l, l, l])
                        elif x < y and y == m and m < l and num_map[y] >= 2:
                            res.append([x, y, y, l])
                        elif y < m:
                            res.append([x, y, m, l])

        if target % 4 == 0:
            n = target // 4 
            if n in num_map and num_map[n] >= 4:
                res.append([n, n, n, n])

        

        return sorted(list(res))