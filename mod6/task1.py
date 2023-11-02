class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None
        self.length = 0

    def push(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node
        self.length += 1

    def get(self, index):
        if index < 0 or index >= self.length:
            raise IndexError("Index out of range")
        current = self.head
        for _ in range(index):
            current = current.next
        return current.data

    def remove(self, index):
        if index < 0 or index >= self.length:
            raise IndexError("Index out of range")
        if index == 0:
            self.head = self.head.next
            self.length -= 1
            return
        current = self.head
        for _ in range(index - 1):
            current = current.next
        current.next = current.next.next
        self.length -= 1

    def insert(self, n, val):
        if n < 0 or n > self.length:
            raise IndexError("Index out of range")
        new_node = Node(val)
        if n == 0:
            new_node.next = self.head
            self.head = new_node
        else:
            current = self.head
            for _ in range(n - 1):
                current = current.next
            new_node.next = current.next
            current.next = new_node
        self.length += 1
