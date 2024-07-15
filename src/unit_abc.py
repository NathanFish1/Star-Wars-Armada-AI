from abc import ABC, abstractmethod
class Unit(ABC):

    @abstractmethod
    def move(self):
        pass
    @abstractmethod
    def actions(self):
        pass
    @abstractmethod
    def draw(self):
        pass