from pydantic import BaseModel, StrictStr


class TranslateModel(BaseModel):
    sentence: StrictStr
