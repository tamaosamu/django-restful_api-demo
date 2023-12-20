from abc import abstractmethod, ABC


class Init(ABC):

    @classmethod
    @abstractmethod
    def get_func_id(cls):
        raise NotImplemented
