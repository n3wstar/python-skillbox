class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None


class Queue:
    def __init__(self):
        self.head = None
        self.tail = None

    def enqueue(self, value):
        new_node = Node(value)
        if self.tail is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node

    def dequeue(self):
        if self.head is None:
            raise IndexError("Queue is empty")
        else:
            dequeued_node = self.head
            self.head = dequeued_node.next
            if self.head is not None:
                self.head.prev = None
            else:
                self.tail = None
            dequeued_node.next = None
            return dequeued_node.value

    def is_empty(self):
        return self.head is None
