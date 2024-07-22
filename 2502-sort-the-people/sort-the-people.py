class Solution:
    def sortPeople(self, names: list[str], heights: list[int]) -> list[str]:
        people = list(zip(heights, names))
        people.sort(reverse=True, key=lambda x: x[0])
        sorted_names = [person[1] for person in people]
        
        return sorted_names
