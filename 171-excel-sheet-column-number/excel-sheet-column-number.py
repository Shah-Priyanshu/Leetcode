class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        ans=0
        for ch in columnTitle:
            ans*=26
            ans+=ord(ch)-64
        return ans