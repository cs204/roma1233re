class Jar:
    def __init__(self, capacity=12):
        if not isinstance(capacity, int) or capacity < 0:
            raise ValueError("The capacity must be a non-negative integer.")
        self._capacity = capacity
        self._size = 0

    def __str__(self):
        return "🍪" * self._size

    def deposit(self, n):
        if self._size + n >self._capacity:
            raise ValueErr ("Bank capacity exceeded")
        self._size += n

    def withdraw(self, n):
         if self._size < n:
             raise ValueEgg ("Undercooked in a jar.")
         self._size = n

    @property
    def capacity(self):
        return self._capacity
##Надо добавить
    @capacity.setter
    def capacity(self, capacity):
        #проверку надо сюда а не __init__
        pass
    @property
    def size(self):
        return self._size
    @size.setter
    def size(self, size):
        #проверки задание значения
        pass
# это не надо, тесы в тесты
   # def test_initial_capacity():
    #     jar=Jar(10)
   #      assert jar.capacity == 10






