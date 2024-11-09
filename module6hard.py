from math import pi, sqrt

class Figure:
    sides_count = 0

    def __init__(self, color: tuple, *sides: int):
        if self.__is_valid_sides(*sides):
            self.__sides = list(sides)
        else:
            self.__sides = [1] * self.sides_count

        if (isinstance(color, tuple)
                and len(color) == 3
                and self.__is_valid_color(*color)):
            self.__color = list(color)
        else:
            self.__color = [127, 127, 127]

        self.filled = True

    def get_color(self):
        return self.__color

    def __is_valid_color(self, r: int, g: int, b: int) -> bool:
        color_range = range(256)
        return r in color_range and g in color_range and b in color_range

    def set_color(self, r: int, g: int, b: int):
        if self.__is_valid_color(r, g, b):
            self.__color = [r, g, b]

    def __is_valid_sides(self, *sides: int) -> bool:
        if len(sides) != self.sides_count:
            return False
        for side_len in sides:
            if not isinstance(side_len, int) and side_len <= 0:
                return False
        return True

    def get_sides(self):
        return self.__sides

    def __len__(self):
        return sum(self.__sides)

    def set_sides(self, *new_sides: int):
        if self.__is_valid_sides(*new_sides):
            self.__sides = list(new_sides)


class Circle(Figure):
    sides_count = 1
    def __init__(self, color: tuple, *sides: int):
        super().__init__(color, *sides)
        self.__radius = len(self) / 2 / pi

    def get_square(self):
        return pi * self.__radius ** 2

    def set_sides(self, *new_sides: int):
        super().set_sides(*new_sides)
        self.__radius = len(self) / 2 / pi


class Triangle(Figure):
    sides_count = 3

    def get_square(self):
        p = len(self) / 2
        a, b, c = self.get_sides()
        return sqrt(p * (p - a) * (p - b) * (p - c))


class Cube(Figure):
    sides_count = 12

    def __init__(self, color: tuple, *sides: int):
        if self.__is_valid_sides(*sides):
            side_len = sides[0]
        else:
            side_len = 1
        super().__init__(color, *((side_len,) * self.sides_count))

    def __is_valid_sides(self, *sides: int) -> bool:
        if len(sides) != 1:
            return False
        else:
            return isinstance(sides[0], int) and sides[0] > 0

    def set_sides(self, *new_sides: int):
        if self.__is_valid_sides(*new_sides):
            super().set_sides(*((new_sides[0],) * self.sides_count))

    def get_volume(self):
        return self.get_sides()[0] ** 3

if __name__ == '__main__':
    circle1 = Circle((200, 200, 100), 10)
    cube1 = Cube((222, 35, 130), 6)

    # Проверка на изменение цветов:
    circle1.set_color(55, 66, 77)  # Изменится
    print(circle1.get_color())
    cube1.set_color(300, 70, 15)  # Не изменится
    print(cube1.get_color())

    # Проверка на изменение сторон:
    cube1.set_sides(5, 3, 12, 4, 5)  # Не изменится
    print(cube1.get_sides())
    circle1.set_sides(15)  # Изменится
    print(circle1.get_sides())

    # Проверка периметра (круга), это и есть длина:
    print(len(circle1))

    # Проверка объёма (куба):
    print(cube1.get_volume())
