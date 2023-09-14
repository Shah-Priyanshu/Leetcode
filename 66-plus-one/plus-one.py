class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        # Initialize carry to 1 to add 1 to the least significant digit
        carry = 1
        
        # Iterate through the digits in reverse order
        for i in range(len(digits) - 1, -1, -1):
            current_sum = digits[i] + carry
            # Update the current digit and reset carry
            digits[i] = current_sum % 10
            carry = current_sum // 10
    
        # If there's a carry left after the loop, add it as a new most significant digit
        if carry > 0:
            digits.insert(0, carry)
    
        return digits