from pydantic import BaseModel


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


class FileCreate(BaseModel):
    name: str
    content: str


class File(FileCreate):
    id: int

    class Config:
        orm_mode = True
