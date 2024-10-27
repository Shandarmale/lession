class House:
    def __init__(self,name,number_of_floor):
        self.name = name
        self.number_of_floor = int(number_of_floor)
    def go_to(self,new_floor):
        int(new_floor)
        if new_floor > self.number_of_floor or new_floor < 1:
            print('Такого этажа не существует')
        else:
            for i in range (1, new_floor + 1):
                print(i)
    def __len__(self):
        return self.number_of_floor
    def __str__(self):
        return f"Название: {self.name}, кол-во этажей:{self.number_of_floor}"
    def __eq__(self, other):
        return isinstance(other, int) and self.number_of_floor == other.number_of_floor
    def __lt__(self, other):
        return self.number_of_floor < other.number_of_floor
    def __le__(self, other):
        return self.number_of_floor <= other.number_of_floor
    def __gt__(self, other):
        return self.number_of_floor > other.number_of_floor
    def __ge__(self, other):
        return self.number_of_floor >= other.number_of_floor
    def __ne__(self, other):
        return self.number_of_floor != other.number_of_floor
    def __add__(self, other):
        if not isinstance(other, int):
            return  House(self.number_of_floor + other)
    def __iadd__(self, other):
        if isinstance(other, int):
            return House(self.number_of_floor + other)
    def __radd__(self, other):
        if not isinstance(other, (int, House)):
            nof = other
        if isinstance(other, House):
            nof = other.number_of_floor
            return  House(self.number_of_floor + nof)





h1 = House('ЖК Эльбрус', 10)
h2 = House('ЖК Акация', 20)

print(h1)
print(h2)

print(h1 == h2) # __eq__

h1 = h1 + 10 # __add__
print(h1)
print(h1 == h2)

h1 += 10 # __iadd__
print(h1)

h2 = 10 + h2 # __radd__
print(h2)

print(h1 > h2) # __gt__
print(h1 >= h2) # __ge__
print(h1 < h2) # __lt__
print(h1 <= h2) # __le__
print(h1 != h2) # __ne__