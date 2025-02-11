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
# Значение выносливости
DEFAULT_STAMINA = 80


class Character:
    """Базовый класс Персонаж."""
    # Константа для диапазона очков урона.
    RANGE_VALUE_ATTACK = (1, 3)
    # Константа для диапазона очков защиты.
    RANGE_VALUE_DEFENCE = (1, 5)
    # Константа для специального умения.
    SPECIAL_SKILL = 'Удача'
    # Константа для значениея очков урона, для базового класса.
    SPECIAL_BUFF = 15
    # Константа для описания класса персонажа.
    BRIEF_DESC_CHAR_CLASS = 'отважный любитель приключений'

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

    def __str__(self):
        """Функция возвращающая имя и описание персонажа."""
        return f'{self.__class__.__name__} - {self.BRIEF_DESC_CHAR_CLASS}.'


class Warrior(Character):
    """Дочерний класс Воин."""
    # Переопределение констант для класса-наследника Воин.
    BRIEF_DESC_CHAR_CLASS = (' дерзкий воин ближнего боя. '
                             'Сильный, выносливый и отважный')
    RANGE_VALUE_ATTACK = (3, 5)
    RANGE_VALUE_DEFENCE = (5, 10)
    SPECIAL_BUFF = DEFAULT_STAMINA + 25
    SPECIAL_SKILL = 'Выносливость'


class Mage(Character):
    """Дочерний класс Маг."""
    # Переопределение констант для класса-наследника Маг.
    BRIEF_DESC_CHAR_CLASS = (' находчивый воин дальнего боя. '
                             'Обладает высоким интеллектом')
    RANGE_VALUE_ATTACK = (5, 10)
    RANGE_VALUE_DEFENCE = (-2, 2)
    SPECIAL_BUFF = DEFAULT_ATTACK + 40
    SPECIAL_SKILL = 'Атака'


class Healer(Character):
    """Дочерний класс Целитель."""
    # Переопределение констант для класса-наследника Целитель.
    BRIEF_DESC_CHAR_CLASS = (' могущественный заклинатель. '
                             'Черпает силы из природы, веры и духов')
    RANGE_VALUE_ATTACK = (-3, -1)
    RANGE_VALUE_DEFENCE = (2, 5)
    SPECIAL_BUFF = DEFAULT_DEFENCE + 30
    SPECIAL_SKILL = 'Защита'


def choice_char_class(char_name: str) -> Character:
    """Возвращает строку с выбранным классом персонажа."""
    # Добавляем словарь, в котором соотносится ввод пользователя
    # и класс персонажа.
    game_classes = {'warrior': Warrior, 'mage': Mage, 'healer': Healer}

    # Переменная принимающая значение одобрен выбор персонажа или нет.
    approve_choice: str = None

    while approve_choice != 'y':
        # Ввод пользователя записывается в отдельную строковую переменную.
        selected_class = input('Введи название персонажа, '
                               'за которого хочешь играть: Воитель — warrior, '
                               'Маг — mage, Лекарь — healer: ')
        # Объект выбранного пользователем класса записывается в переменную.
        char_class: Character = game_classes[selected_class](char_name)
        # Вывели в терминал описание персонажа.
        print(char_class)
        approve_choice = input('Нажми (Y), чтобы подтвердить выбор, '
                               'или любую другую кнопку, '
                               'чтобы выбрать другого персонажа ').lower()
    return char_class


def start_training(character: str) -> Character:
    """Функция тренировки персонажа."""
    # Добавляем словарь, в котором соотносится ввод пользователя
    # и класс персонажа.
    commands = {
                'attack': character.attack,
                'defence': character.defence,
                'special': character.special
    }

    print('Потренируйся управлять своими навыками.')
    print('Введи одну из команд: attack — чтобы атаковать противника, '
          'defence — чтобы блокировать атаку противника или '
          'special — чтобы использовать свою суперсилу.')
    print('Если не хочешь тренироваться, введи команду skip.')

    cmd = None
    while cmd != 'skip':
        # Ввод пользователя записывается в отдельную строковую переменную.
        cmd = input('Введи команду: ')

        if cmd in commands:
            print(commands[cmd]())

    return 'Тренировка окончена.'


# Создан объект класса Воин.
warrior = Warrior('Кодослав')
print(warrior)
# Для объекта Воин вызван метод атаки.
print(warrior.attack())
