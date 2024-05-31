class Solution:
    def fractionToDecimal(self, numerator: int, denominator: int) -> str:
        if numerator == 0:
            return "0"
        
        result = []
         
        if (numerator < 0) ^ (denominator < 0):
            result.append("-")
         
        numerator = abs(numerator)
        denominator = abs(denominator)
         
        integer_part = numerator // denominator
        result.append(str(integer_part))
         
        remainder = numerator % denominator
        if remainder == 0:
            return "".join(result)
        
        result.append(".")
         
        remainder_dict = {}
         
        pos = len(result)
        
        while remainder != 0: 
            if remainder in remainder_dict:
                result.insert(remainder_dict[remainder], "(")
                result.append(")")
                break
             
            remainder_dict[remainder] = pos
             
            remainder *= 10
            quotient = remainder // denominator
            result.append(str(quotient))
             
            remainder %= denominator
            pos += 1
        
        return "".join(result)