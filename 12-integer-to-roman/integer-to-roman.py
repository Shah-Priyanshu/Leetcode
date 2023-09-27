class Solution(object):
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        dup = num
        ans = ""
        
        if dup >= 1000:
            temp = dup//1000
            dup -= temp * 1000
            ans += "M"*temp
        if dup >= 900:
            dup -= 900
            ans += "CM"
        if dup >= 500:
            dup -= 500
            ans += "D"
        if dup >= 400 :
            dup -= 400
            ans += "CD"
        if dup >= 100:
            temp = dup//100
            dup -= temp * 100
            ans += "C"*temp
        if dup >= 90:
            dup -= 90
            ans += "XC"
        if dup >= 50 :
            dup -= 50
            ans += "L"
        if dup >= 40 :
            dup -= 40
            ans += "XL"
        if dup >= 10:
            temp = dup//10
            dup -= temp * 10
            ans += "X"*temp
        if dup >= 9:
            dup -= 9
            ans += "IX"
        if dup >= 5:
            dup -= 5
            ans += "V"
        if dup >= 4:
            dup -= 4
            ans += "IV"
        if dup >= 1:
            temp = dup//1
            dup -= temp * 1
            ans += "I"*temp
        return ans