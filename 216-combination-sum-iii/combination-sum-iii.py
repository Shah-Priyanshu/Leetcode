from typing import List

class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        def backtrack(start, current_combination, current_sum):
            if len(current_combination) == k:
                if current_sum == n:
                    results.append(list(current_combination))
                return
            
            for i in range(start, 10):
                if current_sum + i > n:
                    break
                current_combination.append(i)
                backtrack(i + 1, current_combination, current_sum + i)
                current_combination.pop()
        
        results = []
        backtrack(1, [], 0)
        return results