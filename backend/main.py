from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session

import crud, models, schemas
from database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()


# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.post("/projects/", response_model=schemas.Project)
def create_project(project: schemas.ProjectCreate, db: Session = Depends(get_db)):
    db_project = crud.create_project(
        db,
        repository_owner=project.repository_owner,
        repository_name=project.repository_name,
        creator_github_id=project.creator_github_id,
        progress_commit_hash=project.progress_commit_hash,
    )
    if db_project is None:
        raise HTTPException(status_code=409, detail="Duplicate project")
    return db_project


@app.get("/projects/", response_model=list[schemas.Project])
def read_projects(
    repository_owner: str | None = None,
    repository_name: str | None = None,
    creator_github_id: int | None = None,
    progress_commit_hash: str | None = None,
    db: Session = Depends(get_db),
):
    db_projects = crud.get_projects(
        db,
        repository_owner=repository_owner,
        repository_name=repository_name,
        creator_github_id=creator_github_id,
        progress_commit_hash=progress_commit_hash,
    )
    return db_projects


@app.get("/projects/{project_id}", response_model=schemas.Project)
def read_project(project_id: int, db: Session = Depends(get_db)):
    db_project = crud.get_project(db, project_id=project_id)
    if db_project is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_project


@app.put("/projects/{project_id}", response_model=schemas.Project)
def update_project(project_id: int, project: schemas.ProjectUpdate, db: Session = Depends(get_db)):
    db_project = crud.update_project(db, project_id=project_id, progress_commit_hash=project.progress_commit_hash)
    if db_project is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_project


@app.post("/projects/{project_id}/files/", response_model=schemas.File)
def create_file(project_id: int, file: schemas.FileCreate, db: Session = Depends(get_db)):
    db_file = crud.create_file(db, project_id=project_id, file=file)
    if db_file is None:
        raise HTTPException(status_code=409, detail="Duplicate file")
    return db_file


@app.get("/projects/{project_id}/files/", response_model=list[schemas.File])
def read_files(
    project_id: int,
    db: Session = Depends(get_db),
):
    db_files = crud.get_files(db, project_id=project_id)
    return db_files


@app.delete("/projects/{project_id}/files/")
def delete_files(
    project_id: int,
    db: Session = Depends(get_db),
):
    crud.delete_files(db, project_id=project_id)
    return {"detail": "Success"}
