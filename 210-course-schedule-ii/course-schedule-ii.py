from collections import deque, defaultdict
from typing import List

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        # Create an adjacency list and in-degree array
        adj_list = defaultdict(list)
        in_degree = [0] * numCourses
        
        # Build the graph
        for dest, src in prerequisites:
            adj_list[src].append(dest)
            in_degree[dest] += 1
        
        # Queue for the courses with no prerequisites (in-degree 0)
        zero_in_degree_queue = deque([i for i in range(numCourses) if in_degree[i] == 0])
        
        topological_order = []
        
        while zero_in_degree_queue:
            node = zero_in_degree_queue.popleft()
            topological_order.append(node)
            
            # Reduce the in-degree of the neighboring nodes by 1
            for neighbor in adj_list[node]:
                in_degree[neighbor] -= 1
                # If in-degree becomes 0, add it to the queue
                if in_degree[neighbor] == 0:
                    zero_in_degree_queue.append(neighbor)
        
        # If the topological sort includes all courses, return it
        if len(topological_order) == numCourses:
            return topological_order
        else:
            # There exists a cycle, and hence, it is impossible to finish all courses
            return []
