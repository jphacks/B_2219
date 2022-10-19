from email import message
import string
from pydantic import BaseModel


class ItemBase(BaseModel):
    title: str
    description: str | None = None


class ItemCreate(ItemBase):
    pass


class Item(ItemBase):
    id: int
    owner_id: int

    class Config:
        orm_mode = True


class UserBase(BaseModel):
    email: str


class UserCreate(UserBase):
    password: str


class User(UserBase):
    id: int
    is_active: bool
    items: list[Item] = []

    class Config:
        orm_mode = True


class Repository(BaseModel):
    owner_name: str
    repository_name: str


class File(BaseModel):
    name: str
    content: str

    class Config:
        orm_mode = True


class Commit(BaseModel):
    id: str
    message: str
    files: list[File] = []

    class Config:
        orm_mode = True
