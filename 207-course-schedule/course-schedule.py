class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # Create the adjacency list to represent the graph
        graph = [[] for _ in range(numCourses)]
        for dest, src in prerequisites:
            graph[src].append(dest)
        
        # States: 0 = unvisited, 1 = visiting, 2 = visited
        state = [0] * numCourses
        
        def has_cycle(v):
            if state[v] == 1:  # Found a cycle
                return True
            if state[v] == 2:  # Already checked and no cycle
                return False
            
            # Mark the node as visiting
            state[v] = 1
            # Visit all the neighbors
            for neighbor in graph[v]:
                if has_cycle(neighbor):
                    return True
            
            # Mark the node as visited
            state[v] = 2
            return False
        
        # Check for cycles in each course
        for course in range(numCourses):
            if state[course] == 0:
                if has_cycle(course):
                    return False
        
        return True
