class Node(object):
    def __init__(self, val=0, neighbors=None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

class Solution(object):
    def cloneGraph(self, node):
        if not node:
            return None
        
        visited = {}
        
        def dfs(node):
            # If the node has already been visited, return its clone
            if node in visited:
                return visited[node]
            
            # Clone the node and mark it as visited
            clone = Node(node.val)
            visited[node] = clone
            
            # Iterate through the neighbors of the node
            for neighbor in node.neighbors:
                # Recursively clone the neighbors
                clone.neighbors.append(dfs(neighbor))
            
            return clone
        
        # Start the DFS from the given node
        return dfs(node)
