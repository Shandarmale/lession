import time
from threading import Thread


class Knight(Thread):

    def __init__(self, name, power):
        super().__init__()
        self.kname = name
        self.power = power

    def run(self):
        enemy = 100
        day = 0
        print(f"{self.kname}, на нас напали!")
        for i in range(enemy):
            if enemy > 0:
                time.sleep(1)
                day += 1
                enemy -= self.power
                print(f"{self.kname} сражается {day}... ,"
                      f"осталось {enemy} воинов")
                if enemy <= 0:
                    print(f"{self.kname} одержал победу спустя {day} дней(дня)")


first_knight = Knight('Sir Lancelot', 10)
second_knight = Knight("Sir Galahad", 20)

first_knight.start()
second_knight.start()

first_knight.join()
second_knight.join()
print("Все битвы закончились!")
