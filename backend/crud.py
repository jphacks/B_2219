from sqlalchemy.orm import Session

import models, schemas


def get_project(db: Session, project_id: int):
    return db.query(models.Project).filter(models.Project.id == project_id).first()


def get_projects(
    db: Session,
    repository_owner: str | None = None,
    repository_name: str | None = None,
    creator_github_id: int | None = None,
    progress_commit_hash: str | None = None,
):
    query = db.query(models.Project)
    if repository_owner:
        query = query.filter(models.Project.repository_owner == repository_owner)
    if repository_name:
        query = query.filter(models.Project.repository_name == repository_name)
    if creator_github_id:
        query = query.filter(models.Project.creator_github_id == creator_github_id)
    return query.all()


def create_project(
    db: Session, repository_owner: str, repository_name: str, creator_github_id: int, progress_commit_hash: str
):
    query = db.query(models.Project).filter(
        models.Project.repository_owner == repository_owner,
        models.Project.repository_name == repository_name,
        models.Project.creator_github_id == creator_github_id,
    )
    if not db.query(query.exists()).scalar():
        db_project = models.Project(
            repository_owner=repository_owner,
            repository_name=repository_name,
            creator_github_id=creator_github_id,
            progress_commit_hash=progress_commit_hash,
        )
        db.add(db_project)
        db.commit()
        db.refresh(db_project)
        return db_project


def update_project(db: Session, project_id: int, progress_commit_hash: str):
    query = db.query(models.Project).filter(models.Project.id == project_id)

    if db.query(query.exists()).scalar():
        query.update({models.Project.progress_commit_hash: progress_commit_hash})
        db.commit()
        db.close()
        return query.first()


def create_file(db: Session, project_id: int, file: schemas.FileCreate):
    query = db.query(models.File).filter(
        models.File.project_id == project_id, models.File.name == file.name, models.File.content == file.content
    )
    if not db.query(query.exists()).scalar():
        db_file = models.File(project_id=project_id, name=file.name, content=file.content)
        db.add(db_file)
        db.commit()
        db.refresh(db_file)
        return db_file


def get_files(
    db: Session,
    project_id: int | None = None,
):
    return db.query(models.File).filter(models.File.project_id == project_id).all()


def delete_files(
    db: Session,
    project_id: int | None = None,
):
    db.query(models.File).filter(models.File.project_id == project_id).delete()
    db.commit()
    db.close()
