class Worker:
    def __init__(self, name, surname, position, wage, bonus):
        self.n = name
        self.s = surname
        self.p = position
        self._income = {"wage": float(wage), "bonus": float(bonus)}


class Position(Worker):
    def get_full_name(self):
        worker_name = self.n + " " + self.s
        print(f"Имя и фамилия: {worker_name}")

    def get_total_income(self):
        salary = self._income["wage"] + self._income["bonus"]
        print(f"Общий доход составляет: {salary}")


work_1 = Position(input("Имя сотрудникка? "), input("Фамилия сотрудника? "), input("Должность?"),
                  int(input("Сумма з.п.? ")), int(input("Бонусы? ")))
work_1.get_full_name()
work_1.get_total_income()
