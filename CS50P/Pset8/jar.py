class Jar:
    def __init__(self, capacity=12):
        if capacity < 1:
            raise ValueError("Invalid capacity")
        self._capacity = capacity
        self._size = 0

    def __str__(self):
        return "🍪" * self.size

    def deposit(self, n):
        if n < 0 or self.size + n > self.capacity:
            raise ValueError("Too many cookies")
        self._size += n

    def withdraw(self, n):
        if n < 0 or n > self.size:
            raise ValueError("Not enough cookies")
        self._size -= n

    @property
    def capacity(self):
        return self._capacity

    @property
    def size(self):
        return self._size
