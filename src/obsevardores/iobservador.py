from abc import ABC, abstractmethod


class IObservador(ABC):

    @abstractmethod
    def atualizar(self, dado: str):
        pass
