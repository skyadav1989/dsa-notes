class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def is_empty(self):
        return self.head is None

    def insert_at_beginning(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def insert_at_end(self, data):
        new_node = Node(data)
        if self.is_empty():
            self.head = new_node
            return

        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

    def insert_at_position(self, position, data):
        if position < 0:
            raise ValueError("Position cannot be negative.")

        if position == 0:
            self.insert_at_beginning(data)
            return

        new_node = Node(data)
        current = self.head
        index = 0

        while current and index < position - 1:
            current = current.next
            index += 1

        if current is None:
            raise IndexError("Position out of range.")

        new_node.next = current.next
        current.next = new_node

    def delete_from_beginning(self):
        if self.is_empty():
            raise IndexError("Linked list is empty.")

        deleted_data = self.head.data
        self.head = self.head.next
        return deleted_data

    def delete_from_end(self):
        if self.is_empty():
            raise IndexError("Linked list is empty.")

        if self.head.next is None:
            deleted_data = self.head.data
            self.head = None
            return deleted_data

        current = self.head
        while current.next.next:
            current = current.next

        deleted_data = current.next.data
        current.next = None
        return deleted_data

    def delete_by_value(self, value):
        if self.is_empty():
            raise IndexError("Linked list is empty.")

        if self.head.data == value:
            self.head = self.head.next
            return True

        current = self.head
        while current.next and current.next.data != value:
            current = current.next

        if current.next is None:
            return False

        current.next = current.next.next
        return True

    def search(self, value):
        current = self.head
        position = 0

        while current:
            if current.data == value:
                return position
            current = current.next
            position += 1

        return -1

    def length(self):
        count = 0
        current = self.head

        while current:
            count += 1
            current = current.next

        return count

    def reverse(self):
        previous = None
        current = self.head

        while current:
            next_node = current.next
            current.next = previous
            previous = current
            current = next_node

        self.head = previous

    def display(self):
        elements = []
        current = self.head

        while current:
            elements.append(str(current.data))
            current = current.next

        return " -> ".join(elements) if elements else "Linked list is empty."


if __name__ == "__main__":
    linked_list = LinkedList()

    linked_list.insert_at_end(10)
    linked_list.insert_at_end(20)
    linked_list.insert_at_beginning(5)
    linked_list.insert_at_position(2, 15)

    print("Linked list:", linked_list.display())
    print("Length:", linked_list.length())
    print("Position of 15:", linked_list.search(15))

    linked_list.delete_from_beginning()
    print("After deleting from beginning:", linked_list.display())

    linked_list.delete_from_end()
    print("After deleting from end:", linked_list.display())

    linked_list.delete_by_value(15)
    print("After deleting value 15:", linked_list.display())

    linked_list.reverse()
    print("After reversing:", linked_list.display())
