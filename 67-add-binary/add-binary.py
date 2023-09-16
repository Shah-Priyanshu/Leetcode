class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        # Initialize variables to store the result and carry
        result = []
        carry = 0

        # Start from the end of both strings
        i = len(a) - 1
        j = len(b) - 1

        # Iterate through both strings and handle carry
        while i >= 0 or j >= 0:
            # Get the digits from the strings (or 0 if we have reached the beginning)
            digit_a = int(a[i]) if i >= 0 else 0
            digit_b = int(b[j]) if j >= 0 else 0

            # Calculate the sum using bitwise XOR (^) and carry using bitwise AND (&)
            total = digit_a ^ digit_b ^ carry

            # Calculate the new carry using bitwise OR (|)
            carry = (digit_a & digit_b) | (carry & (digit_a ^ digit_b))

            # Append the current sum to the result as a binary digit
            result.append(str(total))

            # Move to the previous digits in both strings
            i -= 1
            j -= 1

        # If there is still a carry after processing both strings, append it
        if carry:
            result.append(str(carry))

        # Reverse the result and join it to form the final binary string
        return ''.join(result[::-1])
        