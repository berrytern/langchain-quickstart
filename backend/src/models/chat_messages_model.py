from typing import List, Union, Any
from pydantic import BaseModel, StrictStr


class HumanMessageModel(BaseModel):
    human: StrictStr

class AIMessageModel(BaseModel):
    ai: StrictStr

class ChatInputModel(BaseModel):
    message: StrictStr
    history: List[Any] #List[Union[HumanMessageModel, AIMessageModel]]