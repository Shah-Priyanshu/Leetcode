class Solution(object):
    def insertionSortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        nums=[]
        curr=ans=head
        while head:
            nums.append(head.val)
            head=head.next
        nums=sorted(nums)
        for i in range(len(nums)):
            curr.val=nums[i]
            curr=curr.next
        return ans