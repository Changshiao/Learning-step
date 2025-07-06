class Jar:
    def __init__(self, capacity=12):
        self._size=0
        self.capacity=capacity

    def __str__(self):
        return self._size*'🍪'


    def deposit(self, n):
        self.size+=n


    def withdraw(self, n):
        self.size-=n


    @property
    def capacity(self):
            return self._capacity

    @capacity.setter
    def capacity(self,value):
        if value<0:
            raise ValueError
        else:
            self._capacity=value


    @property
    def size(self):
        return self._size

    @size.setter
    def size(self,value):
        if value<0:
            raise ValueError
        if value>self._capacity:
            raise ValueError
        self._size=value
