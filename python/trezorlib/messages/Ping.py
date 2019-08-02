# Automatically generated by pb2py
# fmt: off
from .. import protobuf as p

if __debug__:
    try:
        from typing import Dict, List, Optional
        from typing_extensions import Literal  # noqa: F401
    except ImportError:
        Dict, List, Optional = None, None, None  # type: ignore


class Ping(p.MessageType):
    MESSAGE_WIRE_TYPE = 1

    def __init__(
        self,
        message: str = None,
        button_protection: bool = None,
        pin_protection: bool = None,
        passphrase_protection: bool = None,
    ) -> None:
        self.message = message
        self.button_protection = button_protection
        self.pin_protection = pin_protection
        self.passphrase_protection = passphrase_protection

    @classmethod
    def get_fields(cls) -> Dict:
        return {
            1: ('message', p.UnicodeType, 0),
            2: ('button_protection', p.BoolType, 0),
            3: ('pin_protection', p.BoolType, 0),
            4: ('passphrase_protection', p.BoolType, 0),
        }
