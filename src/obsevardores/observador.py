from abc import ABC, abstractmethod
from typing import List, Dict


class Observador(ABC):

    @abstractmethod
    def atualizar(self, dado: List[Dict]):
        pass
