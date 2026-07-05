import random

class RandomizedSet:

    def __init__(self):
        self.arr = []
        self.pos = {}

    def insert(self, val):
        if val in self.pos:
            return False

        self.arr.append(val)
        self.pos[val] = len(self.arr) - 1
        return True

    def remove(self, val):
        if val not in self.pos:
            return False

        idx = self.pos[val]
        last = self.arr[-1]

        # Move the last element to the removed element's position
        self.arr[idx] = last
        self.pos[last] = idx

        # Remove the last element
        self.arr.pop()
        del self.pos[val]

        return True

    def getRandom(self):
        return random.choice(self.arr)