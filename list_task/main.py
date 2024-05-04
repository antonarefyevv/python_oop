from list import SinglyLinkedList
from list import ListItem

list_items = SinglyLinkedList()

list_items.add_first(3)
list_items.add_first(2)
list_items.add_first(1)

list_items.reverse_list()
list_items.print_list()

node1 = ListItem(1)
node2 = ListItem(2)
node3 = ListItem(3)

node1.next_item = node2
node2.next_item = node3





