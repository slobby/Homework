#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from string import ascii_lowercase, ascii_letters
from typing import Any


class Bird:
    def __init__(self, name: str) -> None:
        self._name = name

    def fly(self):
        print("I can fly")

    def walk(self):
        print("I can walk")

    def __str__(self) -> str:
        return f"{self._name} can walk and fly."


class FlyingBird(Bird):
    def __init__(self, name: str, ration: str = "seeds") -> None:
        self._ration = ration
        super().__init__(name)

    def eat(self):
        print(f"{self._name} eats {self._ration}")

    def __str__(self) -> str:
        return f"{self._name} can walk and fly. And eat {self._ration}."


class NonFlyingBird(FlyingBird):
    def __init__(self, name: str, ration: str = "fish") -> None:
        super().__init__(name, ration)

    def swim(self):
        print(f"{self._name} can swim")

    def __getattribute__(self, name: str) -> Any:
        if name == "fly":
            raise AttributeError
        return super().__getattribute__(name)

    def __str__(self) -> str:
        return f"{self._name} can walk and swim. And eat {self._ration}."


class SuperBird(NonFlyingBird, FlyingBird):
    def __str__(self) -> str:
        return f"{self._name} can walk and fly and swim. And eat {self._ration}."


if __name__ == "__main__":
    b = Bird("Any")
    b.walk()
    print(b)
    p = NonFlyingBird("Penguin", "fish")
    p.swim()
    # p.fly()
    p.eat()
    c = FlyingBird("Canary")
    print(c)
    c.eat()
    s = SuperBird("Gull")
    print(s)
    s.eat()
    print(SuperBird.mro())
