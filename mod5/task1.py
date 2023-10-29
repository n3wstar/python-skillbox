class Stack:
    def __init__(self):
        self.head = None

    def push(self, value):
        new_node = Node(value)
        new_node.next = self.head
        self.head = new_node

    def pop(self):
        if self.head is None:
            raise IndexError("Stack is empty")
        else:
            popped_node = self.head
            self.head = popped_node.next
            popped_node.next = None
            return popped_node.value


class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

