import heapq

class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        min_heap = []
        
        # Add the head of each linked list to the min-heap.
        for i, l in enumerate(lists):
            if l:
                heapq.heappush(min_heap, (l.val, i))
                lists[i] = l.next
        
        # Initialize a dummy node to build the merged list.
        dummy = ListNode()
        current = dummy
        
        # Continue until the min-heap is empty.
        while min_heap:
            # Pop the smallest element from the min-heap.
            val, index = heapq.heappop(min_heap)
            
            # Add the smallest element to the merged list.
            current.next = ListNode(val)
            current = current.next
            
            # If there are more elements in the list at 'index', push the next element to the min-heap.
            if lists[index]:
                heapq.heappush(min_heap, (lists[index].val, index))
                lists[index] = lists[index].next
        
        return dummy.next
