from abc import ABC ,abstractmethod


class MyInterface(ABC):

    @abstractmethod
    def save(self, o):
        pass

    @abstractmethod
    def read(self) -> list:
        pass
