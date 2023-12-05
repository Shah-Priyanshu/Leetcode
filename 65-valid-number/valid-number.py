class Solution(object):
    def isNumber(self, s):
        """
        :type s: str
        :rtype: bool
        """
        s = s.strip()  # Remove leading and trailing whitespaces

        seen_digit = False
        seen_dot = False
        seen_e = False
        seen_digit_after_e = False

        for i, char in enumerate(s):
            if char.isdigit():
                seen_digit = True
                seen_digit_after_e = True
            elif char in ['+', '-']:
                # The sign character must be the first character or after 'e' or 'E'
                if i > 0 and s[i - 1] not in ['e', 'E']:
                    return False
            elif char == '.':
                # Dot cannot appear after 'e' or 'E' and there should not be multiple dots
                if seen_dot or seen_e:
                    return False
                seen_dot = True
            elif char in ['e', 'E']:
                # 'e' or 'E' cannot appear multiple times and must be preceded by a digit
                if seen_e or not seen_digit:
                    return False
                seen_e = True
                seen_digit_after_e = False
            else:
                # Any other character is invalid
                return False

        # The number must have at least one digit, and if 'e' or 'E' is present, there must be a digit after it
        return seen_digit and (not seen_e or seen_digit_after_e)
