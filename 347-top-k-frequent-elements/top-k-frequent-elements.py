class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        # Create a Counter to count the frequency of elements in nums
        frequency_counter = Counter(nums)
        
        # Create a min-heap to store the k most frequent elements
        min_heap = []

        # Iterate through the unique elements in frequency_counter
        for num, freq in frequency_counter.items():
            # Push elements into the heap along with their frequencies
            # Negative frequency is used because heapq is a min-heap
            heapq.heappush(min_heap, (freq, num))

            # If the heap size exceeds k, pop the smallest element
            if len(min_heap) > k:
                heapq.heappop(min_heap)
        
        # Extract the k most frequent elements from the heap
        result = []
        while min_heap:
            result.append(min_heap.pop()[1])
        
        # Reverse the result list to get the elements in the correct order
        result.reverse()

        return result