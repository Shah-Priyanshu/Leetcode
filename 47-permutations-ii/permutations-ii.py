class Solution(object):
    def permuteUnique(self, nums):
        def gen(res, arr): 
            if len(arr) == 0:
                returnRes.append(res)
            check = []
            for i in arr: 
                if i not in check: 
                    temp = res[:]
                    temp.append(i)
                    tempArr = arr[:]
                    tempArr.remove(i) 
                    check.append(i)
                    gen(temp, tempArr)
        returnRes = []
        gen([], nums)
        return returnRes