class Solution(object):
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        # Reverse the input strings for easier multiplication
        num1 = num1[::-1]
        num2 = num2[::-1]

        # Initialize a result array with zeros
        result = [0] * (len(num1) + len(num2))

        # Multiply each digit and update the result array
        for i in range(len(num1)):
            for j in range(len(num2)):
                result[i + j] += int(num1[i]) * int(num2[j])
                result[i + j + 1] += result[i + j] // 10
                result[i + j] %= 10

        # Convert the result array to a string
        while len(result) > 1 and result[-1] == 0:
            result.pop()
        
        return ''.join(map(str, result[::-1]))
