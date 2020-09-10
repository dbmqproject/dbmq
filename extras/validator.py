"""
Validator.

For more information about validator file, check out
https://docs...
"""

from pydantic import BaseModel, ValidationError
from .textstyle import Failure


class Container(BaseModel):
    IMAGE: str
    NAME: str
    NOCACHE: bool = False


class ServerConfigs(BaseModel):
    CONTAINER: Container
    NAME: str
    SERVER: str


def ServerConfigsValidator(configs):
    try:
        data = ServerConfigs(**configs)
        return {'status': True, 'data': data.json()}
    except ValidationError as e:
        return {'status': False, 'data': e}
