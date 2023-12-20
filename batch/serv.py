from .lib.interface.init import Init


class Serv(Init):
    FUNC_ID = "11-22-33-44"

    @classmethod
    def get_func_id(cls):
        return cls.FUNC_ID
