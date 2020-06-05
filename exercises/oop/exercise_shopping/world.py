#/user/bin/python3

# Defines the types Person, Shop, World

import random
import functools

# General helper functions
def get_all_possible_items() -> tuple:
    return (
        'cloth',
        'vegetable',
        'fruit',
        'vehicle',
        'book',
        'pen',
        'pencil',
        'electronics',
        'utensils',
        'home',
        'miscellaneous'
    )

class Person:
    
    def __init__(self, unique_id: int, name: str, money: float = 0.0):
        self.uid = unique_id
        self.name = name
        self.avail_money = money
        self.assert_positive_money()
        self.assert_positive_money()
    
    def assert_positive_money(self):
        assert self.avail_money >= 0

    def add_money(self, money: float):
        self.assert_positive_money()
        self.avail_money += money

    def __str__(self):
        return str(self.name)

class Shop:
    invalid_money: int = -1

    def __init__(self, unique_id: int, name: str, items = []):
        self.uid = unique_id
        self.name = name
        self.items = tuple([(it, Shop.cost(it)) for it in items])

    def generate_random_items(self, generate_f):
        items = generate_f()
        
        self.items = tuple(
            [(it, Shop.cost(it)) if Shop.pos_rand_int() 
            else (it, Shop.invalid_money) for it in items]
        )
        self.items = filter(lambda x: x[1] != Shop.invalid_money, self.items)
    
    def __str__(self):
        return self.name + " | Items:\n" + "\t".join(
            [Shop.get_tuple_as_str(it) for it in self.items]
        )
    
    @classmethod
    def get_tuple_as_str(cls, tup) -> str:
        return ",".join([str(t) for t in tup])

    @classmethod
    def pos_rand_int(cls) -> bool:
        return random.randint(0, 1) == 1
    
    @classmethod
    def cost(cls, item):
        return random.randint(100, 1000)


class World:
    def __init__(self):
        self.people = []
        self.shops = []

    def create_people(self) -> tuple:
        n: int = random.randint(3, 10)
        self.people = [Person(i, 'P-' + str(i)) for i in range(n)]
        return tuple(self.people)

    def create_shops(self) -> tuple:
        n: int = random.randint(3, 10)
        self.shops = [Shop(i, 'S-' + str(i)) for i in range(n)]

        for s in self.shops:
            s.generate_random_items(get_all_possible_items)
            
        return tuple(self.shops)

    def run(self):
        self.create_people()
        self.create_shops()

        for p in self.people:
            print(p)

        for s in self.shops:
            print(s)


def main():
    world = World()
    world.run()


if __name__ == '__main__':
    main()