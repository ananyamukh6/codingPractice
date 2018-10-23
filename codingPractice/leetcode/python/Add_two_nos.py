# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """

        #taking in linked list and return the value at head nad reassigns head to the next val
        carry = 0
        return_sum = None
        return_sum_tail = None
        while l1 is not None or l2 is not None:
            n1 = l1.val if l1 is not None else 0
            n2 = l2.val if l2 is not None else 0
            sumnode_val = n1+n2+carry
            if sumnode_val > 9:
                sumnode_val = sumnode_val - 10
                carry = 1
            else:
                carry = 0
            sumnode = ListNode(sumnode_val)
            if return_sum is None:
                return_sum = sumnode
            else:
                return_sum_tail.next = sumnode
            return_sum_tail = sumnode
            l1 = l1.next if l1 is not None else None
            l2 = l2.next if l2 is not None else None
        if carry == 1:
            return_sum_tail.next = ListNode(1)
        return return_sum
'''
def add_lists(l1, l2):
    sumlist = []
    carry = 0
    for idx in range(0,len(l1)):
        n1 = l1[idx]
        n2 = l2[idx]
        idx_sumval = n1+n2+carry
        if idx_sumval > 9:
            idx_sumval = idx_sumval - 10
            carry = 1
        else:
            carry = 0
        #carry = (0,1)[idx_sumval>9]]
        #idx_sumval = max(idx_sumval - 10, 0)
        sumlist += [idx_sumval]
            

    return sumlist




print(add_lists([1,2,3], [3,2,4]))
'''