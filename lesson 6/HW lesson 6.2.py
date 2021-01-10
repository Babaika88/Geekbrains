class Road:

    def __init__(self, length, width, kv=25, tol=5):
        self._l = length
        self._w = width
        self.kv = kv
        self.tol = tol

    def massa(self):
        n = (self._l * self._w * self.kv * self.tol) / 1000
        print(f"Для покрытия всей дороги потребуется {n} тонн асфальта")


atr = Road(int(input("длинна дороги: ")), int(input("ширина дороги: ")))
atr.massa()
