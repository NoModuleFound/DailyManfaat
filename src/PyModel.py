from pydantic import ConfigDict
from pydantic import BaseModel as BaseConf



class BaseModel(BaseConf):
  model_config = ConfigDict(from_attributes=True)