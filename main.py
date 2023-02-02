"""
В модуле character_creation_module нужно выделить три класса персонажей:
Warrior (воин), Mage (маг) и Healer (целитель).

Персонажи этих классов должны уметь: атаковать, защищаться и
применять специальный навык, который доступен только им.
Умения у всех персонажей одинаковые, но работают они по-разному.
Чтобы эту логику перенести в классы, для каждого класса нужно определить
методы атаки, защиты и специального умения.

Создать базовый класс Character. Объявить в этом классе общие методы и
свойства. Он должен содержать общие атрибуты для всех дочерних классов (name).

Функция attack() должна отвечать за генерацию очков урона,
нанесённого противнику. Принимает на вход имя и класс персонажа.

Функция defence() должна возвращать строку сообщения о блокированном персонажем
уроне в зависимости от его класса.

Функция special() должна возвращать название умения и значение очков урона,
которое наносит это умение.

Классы Warrior, Mage и Healer будут наследниками класса Character.
"""
# Импортируем функцию стандартного модуля random.
from random import randint

# Значение стандартной атаки присваиваем глобальной константе DEFAULT_ATTACK.
DEFAULT_ATTACK = 5
# Значение стандартной защиты присваиваем глобальной константе DEFAULT_DEFENCE.
DEFAULT_DEFENCE = 10


class Character:
    """Базовый класс Персонаж."""
    # Константа для диапазона очков урона.
    RANGE_VALUE_ATTACK = (1, 3)
    # Константа для диапазона очков защиты.
    RANGE_VALUE_DEFENCE = (1, 5)
    # Константа для специального умения.
    SPECIAL_SKILL = 'Удача'
    # Константа для значение очков урона, для базового класса.
    SPECIAL_BUFF = 15

    def __init__(self, name):
        self.name = name

    def attack(self):
        """Функция атаки."""
        # Добавляем переменную value_attack для подсчёта очков урона.
        # # Оператор * распаковывает передаваемый кортеж.
        value_attack = DEFAULT_ATTACK + randint(*self.RANGE_VALUE_ATTACK)
        return (f'{self.name} нанёс противнику урон, равный {value_attack}')

    def defence(self):
        """Функция защиты."""
        # Вычисляем значение защиты в переменной value_defence.
        value_defence = DEFAULT_DEFENCE + randint(*self.RANGE_VALUE_DEFENCE)
        return (f'{self.name} блокировал {value_defence} ед. урона.')

    def special(self):
        """Функция специального умения."""
        return (f'{self.name} применил специальное умение '
                f'"{self.SPECIAL_SKILL} {self.SPECIAL_BUFF}".')


class Warrior(Character):
    """Дочерний класс Воин."""
    def __init__(self):
        ...


class Mage(Character):
    """Дочерний класс Маг."""
    def __init__(self):
        ...


class Healer(Character):
    """Дочерний класс Целитель."""
    def __init__(self):
        ...
