from sqlalchemy.orm import Session

import models, schemas


def get_user(db: Session, user_id: int):
    return db.query(models.User).filter(models.User.id == user_id).first()


def get_user_by_email(db: Session, email: str):
    return db.query(models.User).filter(models.User.email == email).first()


def get_users(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.User).offset(skip).limit(limit).all()


def create_user(db: Session, user: schemas.UserCreate):
    fake_hashed_password = user.password + "notreallyhashed"
    db_user = models.User(email=user.email, hashed_password=fake_hashed_password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


def get_items(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Item).offset(skip).limit(limit).all()


def create_user_item(db: Session, item: schemas.ItemCreate, user_id: int):
    db_item = models.Item(**item.dict(), owner_id=user_id)
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item


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
