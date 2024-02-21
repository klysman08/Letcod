class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def middleNode(self, head: ListNode) -> ListNode:
        a = []
        while head:
            a.append(head)
            print(a)
            head = head.next
            print(head)
        return a[len(a)//2]

head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
middle = Solution()
print(middle.middleNode(head).val)
#print type(middle.middleNode(head))
print(middle.middleNode(head).next.val)



""" 
def middle(head):
    count = 0

    for i in head:
        count += 1
        i +=1

    if count % 2 == 0:
        mid = count // 2
        second_part = head[mid:]
        return second_part
        
    else:
        mid = (count // 2) 
        second_part = head[mid:]
        return second_part
          


print(middle(head = [1,2,3,4,5,6,7])) """

