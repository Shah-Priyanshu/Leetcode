class Solution:
    def luckyNumbers(self, matrix: List[List[int]]) -> List[int]:
        lucky_numbers = []

        # Find the minimum value in each row
        for row in matrix:
            min_value = min(row)
            min_index = row.index(min_value)

            # Check if this minimum value is also the maximum in its column
            is_lucky = True
            for r in matrix:
                if r[min_index] > min_value:
                    is_lucky = False
                    break
            
            if is_lucky:
                lucky_numbers.append(min_value)

        return lucky_numbers
