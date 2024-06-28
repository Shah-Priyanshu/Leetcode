from typing import List
from collections import defaultdict

class Solution:
    def maximumImportance(self, n: int, roads: List[List[int]]) -> int:
        # Step 1: Count the degrees
        degree_count = [0] * n
        for a, b in roads:
            degree_count[a] += 1
            degree_count[b] += 1
        
        # Step 2: Sort cities by their degree in descending order
        sorted_cities = sorted(range(n), key=lambda x: degree_count[x], reverse=True)
        
        # Step 3: Assign values from n to 1 to the cities based on their degree
        value_assignment = [0] * n
        current_value = n
        for city in sorted_cities:
            value_assignment[city] = current_value
            current_value -= 1
        
        # Step 4: Calculate the total importance
        total_importance = 0
        for a, b in roads:
            total_importance += value_assignment[a] + value_assignment[b]
        
        return total_importance
