"""
Validator.

For more information about validator file, check out
https://docs...
"""

import json

from pydantic import BaseModel, ValidationError

from .textstyle import Failure


# pydantic base models
class Container(BaseModel):
    IMAGE: str
    NAME: str
    NOCACHE: bool = False


class ServerConfigs(BaseModel):
    CONTAINER: Container
    NAME: str
    SERVER: str


# validators based on pydantic base models
def ServerConfigsValidator(configs):
    try:
        data = ServerConfigs(**configs)
        data = json.loads(data.json())
        return {'status': True, 'data': data}
    except ValidationError as e:
        return {'status': False, 'data': e}
