class Solution(object):
    def sortedListToBST(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[TreeNode]
        """

        if not head:
            return
        inorder = []
        while head:
            inorder.append(head.val)
            head = head.next

        return self.BST(inorder)

        
    def BST(self, inorder):
        if not inorder:
            return
        idx = len(inorder) // 2
        node = TreeNode(inorder[idx])
        node.left = self.BST(inorder[:idx])
        node.right = self.BST(inorder[idx+1:])
        
        return node