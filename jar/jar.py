class Jar:
    # capacidade nao pode ser negativa, se for = value error
    def __init__(self, capacity=12):
        if capacity < 0:
            raise ValueError
        self._capacity = capacity
        self._size = 0

    # retorna str com n cookies, retorna emojis
    def __str__(self):
        return "🍪" * self.size

    # adiciona cookies na jarra, se for maior q a capacidade, value error
    def deposit(self, n):
        if n > self.capacity or n + self.size > self.capacity:
            raise ValueError
        self._size += n

    # remover cookies da jarra, se nao existir mais cookies la, value error
    def withdraw(self, n):
        if n > self.size:
            raise ValueError
        self._size -= n

    # capacidade max da jarra (dps do calculo)
    @property
    def capacity(self):
        return self._capacity

    # o numero atual de cookies na jarra
    @property
    def size(self):
        return self._size

if __name__ == "__main__":
    main()
