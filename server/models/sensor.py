from pydantic import BaseModel, Field

class HumidtySchema(BaseModel):
    value: str = Field(...)