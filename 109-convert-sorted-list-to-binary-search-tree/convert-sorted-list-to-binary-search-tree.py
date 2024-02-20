class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def sortedListToBST(self, head):
        # Function to convert linked list to array
        def mapListToArray(head):
            arr = []
            while head:
                arr.append(head.val)
                head = head.next
            return arr
        
        # Function to convert sorted array to BST
        def sortedArrayToBST(arr, start, end):
            if start > end:
                return None

            mid = (start + end) // 2
            node = TreeNode(arr[mid])
            node.left = sortedArrayToBST(arr, start, mid - 1)
            node.right = sortedArrayToBST(arr, mid + 1, end)
            return node

        # Convert the linked list to an array
        arr = mapListToArray(head)

        # Build the BST from the array
        return sortedArrayToBST(arr, 0, len(arr) - 1)
