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


class ProjectCreate(BaseModel):
    repository_owner: str
    repository_name: str
    creator_github_id: int
    progress_commit_hash: str


class ProjectUpdate(BaseModel):
    progress_commit_hash: str


class Project(ProjectCreate):
    id: int

    class Config:
        orm_mode = True


class File(BaseModel):
    id: int
    project_id: int
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
