from abc import abstractmethod, ABC
from typing import Any, Dict, TypeVar, Generic

T = TypeVar("T")  # Tipo do objeto retornado por conectar_site
R = TypeVar("R")  # Tipo do resultado final (ex: Dict[str, Any])


class IWebScraping(ABC, Generic[T, R]):

    @abstractmethod
    def conectar_site(self) -> T:
        """
        Método para conectar no site
        :return: objeto de conexão
        :rtype: T
        """
        pass

    @abstractmethod
    def obter_dados(self, dados: T) -> R:
        """
        Método para obter dados
        :param dados: objeto dados
        :type dados: T
        :return: dados extraidos do site
        :rtype: R
        """
        pass
