class Solution:
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        left, right = 0, len(s) - 1

        while left < right:
            # Move left pointer to the next alphanumeric character or break if done
            while left < right and not s[left].isalnum():
                left += 1
            # Move right pointer to the previous alphanumeric character or break if done
            while right > left and not s[right].isalnum():
                right -= 1

            # Compare characters in a case-insensitive manner
            if s[left].lower() != s[right].lower():
                return False

            left += 1
            right -= 1

        return True
