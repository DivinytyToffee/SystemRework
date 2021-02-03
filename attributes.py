class Attributes(object):
    """
    Сокращения:
    Очки персонажа(ОП);
    Очки действия(ОД);
    Писихические очки действия(ПОД);

    Первичные атрибуты персонажа, отражающие его базовые харрактеристики;

    Они отражают основные направления его развития,
    а так же из них вычисляются другие харрактеристики;

    Стоймость: следующий уровень умноженное на три(3);

    Характеристики:
    Тело - все проверки связанные с физическим телом.
    Урон, здоровье, ловкость и т.д.;

    Дух - духовные способности.
    Разум - ментальные способности.

    Здоровье - количество урона которое человек способен перенести персонаж.
    Выражается в количестве ран.
    Изначальное количество ран равно двум(2), за каждые три очка в атрибуте ТЕЛО
    персонаж получает дополнительную рану;

    Духовная крепкость - количество духовного урона, т.е,
    урона приходящегося на душу, которое способен перенсти персонаж.
    Выражается в духовных ранах.
    Начальное кол-во ран равно одной(1), за каждые три очка в атрибуте ДУХ
     персонаж получает дополнительную духовную рану;

    ОД - показывает сколько действий может совершить персовнаж за один ход.
    Изначальное колличество ОД равно трём(3), за каждые два очка в атрибуте ТЕЛО
    персонаж получает дополнительное ОД;

    ПОД - показывает сколько психических(духовных) действий может совершить
     персонаж за один ход.
    Под психическими действиями подразумевается использования псайкерских
     талантов или им подобные. Эти действия происходят практически мгновенно,
     но для использования одного ПОДа требуется потратить, как минимум, один ОД.

    """

    def __init__(self, body=1, spirit=1, mind=1):
        # Задаваемые значения
        self.__body = body
        self.__spirit = spirit
        self.__mind = mind

        # Вычисляемые значения
        self.__wounds = 0
        self.__action_points = 0
        self.__psy_action_points = 0
        self.__spiritual_wounds = 0
        self.__mind_wounds = 0

        # Мультипликаторы
        self.__points_multiple = 3

        self.__wounds_multiple = 3
        self.__start_wounds = 2

        self.__action_points_multiple = 4
        self.__start_action_points = 3

        self.__psy_action_points_multiple = 3
        self.__start_psy_action_points = 1

        self.__spiritual_wounds_multiple = 3
        self.__start_spiritual_wounds = 1

        self.__mind_wounds_multiple = 2
        self.__start_mind_wounds = 5

        # Вычисления
        self.__count_wounds()
        self.__count_action_points()
        self.__count_psy_action_points()
        self.__count_spiritual_wounds()
        self.__count_mind_wounds()

    @property
    def wounds(self):
        return self.__wounds

    def __count_wounds(self):
        increase_wounds = self.body // self.__wounds_multiple
        self.__wounds += self.__start_wounds + increase_wounds

    @property
    def action_points(self):
        return self.__action_points

    def __count_action_points(self):
        increase_action_points = self.body // self.__action_points_multiple
        self.__action_points += self.__start_action_points + \
                                increase_action_points

    @property
    def psy_action_points(self):
        return self.__psy_action_points

    def __count_psy_action_points(self):
        increase_psy_action_points = self.body // \
                                     self.__psy_action_points_multiple
        self.__psy_action_points += self.__start_psy_action_points + \
                                    increase_psy_action_points

    @property
    def spiritual_wounds(self):
        return self.__spiritual_wounds

    def __count_spiritual_wounds(self):
        increase_spiritual_wounds = self.spirit // \
                                    self.__spiritual_wounds_multiple
        self.__spiritual_wounds += self.__start_spiritual_wounds \
                                   + increase_spiritual_wounds

    @property
    def mind_wounds(self):
        return self.__mind_wounds

    def add_mind_wounds(self, wound):
        self.__mind_wounds += wound

    def __count_mind_wounds(self):
        increase_mind_wounds = self.mind // self.__mind_wounds_multiple
        self.__mind_wounds += self.__start_mind_wounds + increase_mind_wounds

    def cost(self, value):
        return sum([x * self.__points_multiple for x in range(2, value + 1)])

    @property
    def print_attributes(self):
        return f"Здоровье - {self.wounds} " \
               f"Духовная крепкость - {self.spiritual_wounds} " \
               f"Стабильность рассудка - {self.mind_wounds}\n\n" \
               f"ОД - {self.action_points} " \
               f"ПОД - { self.psy_action_points }" \
               f"\n\n" \
               f"Тело({self.body}) " \
               f"Дух({self.spirit}) " \
               f"Разум({self.mind})\n"

    @property
    def full_cost(self):
        return self.cost(self.body) \
               + self.cost(self.mind) \
               + self.cost(self.spirit)

    @property
    def body(self):
        return self.__body

    @body.setter
    def body(self, value: int):
        self.__body = value

    @body.deleter
    def body(self):
        del self.__body

    @property
    def spirit(self):
        return self.__spirit

    @spirit.setter
    def spirit(self, value: int):
        self.__spirit = value

    @spirit.deleter
    def spirit(self):
        del self.__spirit

    @property
    def mind(self):
        return self.__mind

    @mind.setter
    def mind(self, value: int):
        self.__mind = value

    @mind.deleter
    def mind(self):
        del self.__mind
