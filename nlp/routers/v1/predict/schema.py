from pydantic import BaseModel

class Uses(BaseModel):
    source_ref: str
    target_ref: str