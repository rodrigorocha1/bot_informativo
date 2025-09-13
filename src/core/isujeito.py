from abc import ABC, abstractmethod

from src.obsevardores.iobservador import IObservador


class ISujeito(ABC):

    @abstractmethod
    def anexar(self, observador: IObservador):
        pass

    @abstractmethod
    def desanexar(self, observador: IObservador):
        pass

    @abstractmethod
    def notificar(self, dado: str):
        pass
