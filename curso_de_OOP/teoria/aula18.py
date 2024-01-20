# Interfaces

from abc import ABC, abstractclassmethod

class FormasInterface(ABC):

    @abstractclassmethod
    def get_perimetro(self) -> int:
        pass

    @abstractclassmethod
    def get_area(self) -> int:
        pass
