class SinglyLinkedList:
    def __init__(self):
        self.__head = None
        self.__count = 0

    @property
    def head(self):
        return self.__head

    @head.setter
    def head(self, head):
        self.__head = head

    @property
    def count(self):
        current_item = self.__head
        value = 0
        while current_item is not None:
            value += 1
            current_item = current_item.next_item
        self.__count = value
        return self.__count

    @count.setter
    def count(self, count):
        self.__count = count

    def size(self):
        return self.__count

    def print_list(self):
        current_item = self.__head
        items_list = []
        while current_item is not None:
            items_list.append(str(current_item.data))
            current_item = current_item.next_item
        items_string = ", ".join(items_list)
        print(f'[{items_string}]')

    def add_first(self, head):
        self.__head = ListItem(head, self.__head)

    def delete_first(self):
        head = self.__head
        if head is None:
            return None

        self.__head = head.next_item
        return head.data

    def search(self, index):
        if index > self.count:
            return None

        item = self.__head
        item_index = 0

        while item_index <= index:
            if item_index == index:
                return item.data

            item_index += 1
            item = item.next_item

    def change(self, index, value):
        if index > self.count:
            return None

        if index == 0:
            self.add_first(value)
        item = self.__head
        item_index = 0

        while item_index <= index:
            if item_index == index:
                item.data = value
            item_index += 1
            item = item.next_item

    def insert(self, index, value):
        current_item = self.__head
        if index > self.count:
            return None
        elif current_item is None:
            self.__head = ListItem(value, None)
        elif index == 0:
            self.add_first(value)
        else:
            while current_item.next_item is not None and index > 1:
                current_item = current_item.next_item
                index -= 1

            current_item.next_item = ListItem(value, current_item.next_item)

    def remove_at(self, index):
        if self.__head is None:
            return None
        elif index > self.count:
            return None
        elif index == 0:
            self.delete_first()
        else:
            current_item = self.__head
            while current_item.next_item is not None and index > 1:
                current_item = current_item.next_item
                index -= 1

            value = current_item.next_item.data
            current_item.next_item = current_item.next_item.next_item
            return value

    def reverse_list(self):
        if self.__head is None:
            return

        head = self.__head
        new_head = head.reverse_list()
        head.next_item = None
        self.__head = new_head

    def remove_list_item(self, value):
        if self.__head is None:
            return

        current_node = self.__head
        previous_node = None

        while current_node is not None:
            if current_node.data == value:
                if previous_node is None:
                    self.__head = current_node.next_item
                    return True
                else:
                    previous_node.next_item = current_node.next_item

            previous_node = current_node
            current_node = current_node.next_item


class ListItem:
    def __init__(self, data, next_item=None):
        self.__data = data
        self.__next_item = next_item

    @property
    def data(self):
        return self.__data

    @data.setter
    def data(self, data):
        self.__data = data

    @property
    def next_item(self):
        return self.__next_item

    @next_item.setter
    def next_item(self, next_item):
        self.__next_item = next_item

    def __repr__(self):
        return f'[{self.__data}, {self.__next_item}]'

    def reverse_list(self):
        if self is not None:
            head = self
            tail = None
            while head is not None:
                head.next_item, tail, head = tail, head, head.next_item

            return tail

    def print_list_item(self):
        print(self.data)

    def remove_list_item_by_value(self, value):
        head = self
        tail = head.next_item
        while head is not None:
            if head.data == value:
                tail = tail.next_item
                tail.next_item = None
                return tail
            else:
                head.data = tail
        return True
