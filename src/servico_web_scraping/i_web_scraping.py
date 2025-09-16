from abc import abstractmethod, ABC
from typing import TypeVar, Generic, Tuple

T = TypeVar("T")  # Tipo do objeto retornado por conectar_site


class IWebScraping(ABC, Generic[T]):

    @abstractmethod
    def conectar_site(self) -> Tuple[T, int] | str:
        """
        Método para conectar no site
        :return: objeto de conexão
        :rtype: T
        """
        pass

    @abstractmethod
    def obter_dados(self, dados: T):
        """
        Método para obter dados
        :param dados: objeto dados
        :type dados: T

        """
        pass
