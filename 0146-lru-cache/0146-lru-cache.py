class Node:
    def __init__(self, key=0, value=0):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None


class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}

        # Dummy head and tail
        self.head = Node()
        self.tail = Node()

        self.head.next = self.tail
        self.tail.prev = self.head

    # Add node right after head
    def add(self, node):
        node.next = self.head.next
        node.prev = self.head

        self.head.next.prev = node
        self.head.next = node

    # Remove node from list
    def remove(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev

    # Move node to the front
    def move_to_front(self, node):
        self.remove(node)
        self.add(node)

    def get(self, key: int) -> int:

        if key not in self.cache:
            return -1

        node = self.cache[key]

        # Recently used
        self.move_to_front(node)

        return node.value

    def put(self, key: int, value: int) -> None:

        # Key already exists
        if key in self.cache:
            node = self.cache[key]

            node.value = value
            self.move_to_front(node)
            return

        # Create new node
        node = Node(key, value)

        self.cache[key] = node
        self.add(node)

        # Capacity exceeded
        if len(self.cache) > self.capacity:

            # LRU node is right before tail
            lru = self.tail.prev

            self.remove(lru)
            del self.cache[lru.key]