from sqlalchemy import Boolean, Column, Integer, String

from database import Base


class Project(Base):
    __tablename__ = "projects"

    id = Column(Integer, primary_key=True, index=True)
    repository_owner = Column(String, index=True)
    repository_name = Column(String, index=True)
    creator_github_id = Column(Integer, index=True)
    progress_commit_hash = Column(String, index=True)


class File(Base):
    __tablename__ = "files"

    id = Column(Integer, primary_key=True, index=True)
    project_id = Column(Integer, index=True)
    name = Column(String, index=True)
    content = Column(String, index=True)
