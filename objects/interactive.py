from abc import ABC, abstractmethod


class Interactive(ABC):

    @abstractmethod
    def interact(self, engine, hero):
        pass
