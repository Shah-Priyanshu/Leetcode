from heapq import heappush, heappop

class Solution:
    def getSkyline(self, buildings: List[List[int]]) -> List[List[int]]:
        # Generate the events
        events = []
        for left, right, height in buildings:
            events.append((left, -height, right))  # Start event
            events.append((right, 0, 0))  # End event
        
        # Sort the events: first by x coordinate, then by height
        events.sort()
        
        # Result list and a max-heap to keep track of the buildings' heights
        result = []
        heap = [(0, float('inf'))]  # (height, end) pair; initially with ground level height
        
        for x, neg_height, right in events:
            # If it is the start of the building, add the building height to the heap
            if neg_height != 0:
                heappush(heap, (neg_height, right))
            
            # Remove the building heights which are outdated
            while heap[0][1] <= x:
                heappop(heap)
            
            # Get the current max height
            current_height = -heap[0][0]
            
            # If the current height differs from the last added height in the result, add a new point
            if not result or result[-1][1] != current_height:
                result.append([x, current_height])
        
        return result
