from linked_list import Node, LinkedList

llist = LinkedList()

llist.head = Node("Dushanba")
tuesday = Node("Seshanba")
wednesday = Node("Chorshanba")
llist.head.next = tuesday
tuesday.next = wednesday
# print(llist.printList())
llist.first_push("Yakshanba")
# print(llist.printList())
llist.insert_after(llist.head.next, "yangi")
llist.last_append("ohirgi")
llist.delete('Seshanba')
print(llist.printList())
