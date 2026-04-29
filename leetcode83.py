class Listnode:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next


def deleteDuplicates(head):
    temp = head

    while temp.next != None:
        temp1 = temp
        while temp1.val == temp1.next.val:
            temp1 = temp1.next
        temp.next = temp1.next
        temp = temp.next

    return head


a = Listnode(16)
b = Listnode(16)
c = Listnode(16)
d = Listnode(16)
e = Listnode(18)
a.next = b
b.next = c
c.next = d
d.next = e


temp = deleteDuplicates(a)
while temp != None:
    print(temp.val)
    temp = temp.next
