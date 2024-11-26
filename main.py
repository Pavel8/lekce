from abc import ABC, abstractmethod

class View(ABC):
    def __init__(self, name: str, position: tuple):
        self.name = name
        self.position = position

    @abstractmethod
    def move(self, new_position: tuple):

class Zobrazitelny:

    @abstractmethod
    def show(self):
        print("Informace")

class Button(View, Zobrazitelny):

