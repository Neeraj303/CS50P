class Jar:
    def __init__(self, capacity=12, size=0):
        if isinstance(capacity, int) and capacity > 0 and size <= capacity:
            self.capacity = capacity
            self.size = size
        else:
           raise ValueError

    def __str__(self):
        return "🍪"*self.size

    def initially(self, initial=0):
        self.initial = initial

    def deposit(self, n):
        if self.capacity < self.size + n:
            raise ValueError
        self.size = self.size + n


    def withdraw(self, n):
        if self.size < n:
            raise ValueError
        self.size = self.size - n

    @property
    def capacity(self):
        return self._capacity

    @capacity.setter
    def capacity(self, capacity):
        self._capacity = capacity

    @property
    def size(self):
        return self._size

    @size.setter
    def size(self, size):
        self._size = size

jar = Jar()
jar.deposit(1)
print(jar.size)



