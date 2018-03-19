#                 ┌───────────────┐
#                 │    Animal     │
#                 └───────────────┘
#                         │
#            ┌────────────┴────────────┐
#            │                         │
#            ▼                         ▼
#     ┌─────────────┐           ┌─────────────┐
#     │   Mammal    │           │    Bird     │
#     └─────────────┘           └─────────────┘
#            │                         │
#      ┌─────┴──────┐            ┌─────┴──────┐
#      │            │            │            │
#      ▼            ▼            ▼            ▼
# ┌─────────┐  ┌─────────┐  ┌─────────┐  ┌─────────┐
# │   Dog   │  │   Bat   │  │ Parrot  │  │ Ostrich │
# └─────────┘  └─────────┘  └─────────┘  └─────────┘
#                 ┌───────────────┐
#                 │    Animal     │
#                 └───────────────┘
#                         │
#            ┌────────────┴────────────┐
#            │                         │
#            ▼                         ▼
#     ┌─────────────┐           ┌─────────────┐
#     │  Runnable   │           │   Flyable   │
#     └─────────────┘           └─────────────┘
#            │                         │
#      ┌─────┴──────┐            ┌─────┴──────┐
#      │            │            │            │
#      ▼            ▼            ▼            ▼
# ┌─────────┐  ┌─────────┐  ┌─────────┐  ┌─────────┐
# │   Dog   │  │ Ostrich │  │ Parrot  │  │   Bat   │
# └─────────┘  └─────────┘  └─────────┘  └─────────┘


class Animal(object):
    pass


# 大类:
class Mammal(Animal):
    pass


class Bird(Animal):
    pass


# 爬行类
class Runnable(object):
    def run(self):
        print('Running...')


# 飞行类
class Flyable(object):
    def fly(self):
        print('Flying...')


# 各种动物:
class Dog(Mammal, Runnable):
    pass


class Bat(Mammal, Flyable):
    pass


class Parrot(Bird):
    pass


class Ostrich(Bird):
    pass


def main():
    dog = Dog()
    dog.run()


if __name__ == '__main__':
    main()

