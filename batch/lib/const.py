from enum import Enum


class Status(Enum):
    RUNNING = "00"
    SUCCESS = "01"
    EXCEPTION = "90"


class Message(Enum):
    E7601 = "{} {} "
    E7611 = "{} {} {}"
    E7615 = "{}"
    E7603 = "{} {}"
