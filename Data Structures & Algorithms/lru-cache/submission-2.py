class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.currentCapacity = 0
        self.hash = {}
        self.lru = None
        self.lruTail = None

    def addLru(self, key):
        node = ListNode(key)

        if not self.lru:
            self.lru = node
            self.lruTail = node
        else:
            self.lruTail.next = node

            # ADDED/CHANGED: Assign the new node directly as the tail
            self.lruTail = node

    def updateLru(self, key):
        node = self.lru
        prev = None

        # ADDED/CHANGED: Check the key while ensuring node exists
        while node and node.val != key:
            prev = node
            node = node.next

        # ADDED: Handle missing nodes and nodes already at the tail
        if not node or node is self.lruTail:
            return

        # Remove node from its current position
        if prev:
            prev.next = node.next
        else:
            # ADDED/CHANGED: Move the head when the first node is accessed
            self.lru = node.next

        # ADDED: Detach the node from its old position
        node.next = None

        # ADDED: Append the node to the tail
        self.lruTail.next = node

        # ADDED/CHANGED: Update the tail directly
        self.lruTail = node

    def get(self, key: int) -> int:
        if key not in self.hash:
            return -1

        self.updateLru(key)
        return self.hash[key]

    def put(self, key: int, value: int) -> None:
        if key in self.hash:
            # ADDED/CHANGED: Update the value for an existing key
            self.hash[key] = value
            self.updateLru(key)
            return

        if self.currentCapacity == self.capacity:
            # Evict the least recently used key
            lru_key = self.lru.val
            del self.hash[lru_key]
            self.lru = self.lru.next

            # ADDED: Decrease capacity after eviction
            self.currentCapacity -= 1

            # ADDED: Reset tail when eviction empties the list
            if not self.lru:
                self.lruTail = None

        self.addLru(key)
        self.hash[key] = value

        # ADDED/CHANGED: Increment capacity after inserting a new key
        self.currentCapacity += 1