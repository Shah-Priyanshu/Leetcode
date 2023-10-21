class Solution(object):
    def combinationSum(self, candidates, target):
        def backtrack(remaining_target, current_combination, start):
            if remaining_target == 0:
                result.append(current_combination[:])
                return
            if remaining_target < 0:
                return

            for i in range(start, len(candidates)):
                current_combination.append(candidates[i])
                backtrack(remaining_target - candidates[i], current_combination, i)
                current_combination.pop()

        result = []
        candidates.sort()  # Sort the candidates to handle duplicates efficiently
        backtrack(target, [], 0)
        return result