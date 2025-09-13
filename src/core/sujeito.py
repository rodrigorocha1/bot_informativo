from abc import ABC
from typing import List, Dict

from src.obsevardores.observador import Observador


class Sujeito(ABC):

    def __init__(self):
        self._observadores: List[Observador] = []

    def anexar(self, observador: Observador):
        self._observadores.append(observador)

    def remover(self, observador: Observador):
        self._observadores.remove(observador)

    def notificar(self, dado: str):
        for observador in self._observadores:
            observador.atualizar(dado)
