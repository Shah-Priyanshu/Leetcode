class Solution:
    def averageWaitingTime(self, customers: List[List[int]]) -> float:
        total_waiting_time = 0
        current_time = 0
        
        for arrival, time_needed in customers:
            # Ensure the chef starts at the right time
            current_time = max(current_time, arrival) + time_needed
            # Calculate waiting time for this customer
            total_waiting_time += current_time - arrival
        
        # Calculate the average waiting time
        return total_waiting_time / len(customers)
