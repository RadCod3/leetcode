from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __str__(self) -> str:
        vals = []
        curr = self
        while curr.next:
            vals.append(curr.val)
            curr = curr.next
        vals.append(curr.val)
        return str(vals)


def addTwoNumbers(l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
    carry = 0
    ans = ListNode()
    ans_ptr = ans
    while l1.next != None and l2.next != None:
        sum = l1.val + l2.val + carry
        if sum >= 10:
            ans_ptr.val = sum - 10
            carry = 1
        else:
            carry = 0
            ans_ptr.val = sum
        ans_ptr.next = ListNode()
        ans_ptr = ans_ptr.next
        l1 = l1.next
        l2 = l2.next

    sum = l1.val + l2.val + carry
    ans_ptr.val = sum

    # l1 or l2 has more nodes than the other
    if l2.next != None or l1.next != None:
        if l2.next != None:
            ans_ptr.next = l2.next
        elif l1.next != None:
            ans_ptr.next = l1.next

    if sum >= 10:
        ans_ptr.val -= 10
        carry_ = 1
        if ans_ptr.next == None:
            ans_ptr.next = ListNode()
        ans_ptr = ans_ptr.next
        while carry_ == 1:
            ans_ptr.val += 1
            if ans_ptr.val >= 10:
                ans_ptr.val -= 10
                if ans_ptr.next == None:
                    ans_ptr.next = ListNode()
                ans_ptr = ans_ptr.next
            else:
                break

    return ans


l1 = ListNode(
    9, ListNode(9, ListNode(9, ListNode(9, ListNode(9, ListNode(9, ListNode(9))))))
)
l2 = ListNode(9, ListNode(9, ListNode(9, ListNode(9))))
# print(l1)
# print(l2)

print(
    addTwoNumbers(
        ListNode(2, ListNode(4, ListNode(3))), ListNode(5, ListNode(6, ListNode(4)))
    )
)
