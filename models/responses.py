from pydantic import BaseModel,Field
class SuccessResponse(BaseModel):
    status_code: int= Field(default=200)
    message: str
    data: dict


class ErrorResponse(BaseModel):
    status_code: int = Field(default=500)
    message: str
    data: dict = Field(default={})