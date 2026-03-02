from pydantic import BaseModel


class UserCreate(BaseModel):
    username: str


class TaskCreate(BaseModel):
    title: str


class TaskOut(BaseModel):
    id: int
    title: str
    status: str

    model_config = {
        "from_attributes": True
    }
    
