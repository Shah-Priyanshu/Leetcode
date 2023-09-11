class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        roman_values = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }

        total = 0
        prev_value = 0

        # Iterate through the input string from right to left
        for symbol in s[::-1]:
            current_value = roman_values[symbol]

            # If the current value is smaller than the previous value,
            # subtract it; otherwise, add it to the total
            if current_value < prev_value:
                total -= current_value
            else:
                total += current_value

            # Update the previous value for the next iteration
            prev_value = current_value

        return total