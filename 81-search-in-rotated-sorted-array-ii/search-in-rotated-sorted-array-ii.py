class Solution(object):
    def search(self, nums, target):
        left, right = 0, len(nums) - 1

        while left <= right:
            mid = (left + right) // 2

            if nums[mid] == target:
                return True

            # If the left half is sorted
            if nums[left] < nums[mid]:
                if nums[left] <= target <= nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
            # If the right half is sorted
            elif nums[left] > nums[mid]:
                if nums[mid] <= target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1
            # Handle the case where there are duplicates
            else:
                left += 1

        return False