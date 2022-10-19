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


@app.post("/users/", response_model=schemas.User)
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    db_user = crud.get_user_by_email(db, email=user.email)
    if db_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    return crud.create_user(db=db, user=user)


@app.get("/users/", response_model=list[schemas.User])
def read_users(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    users = crud.get_users(db, skip=skip, limit=limit)
    return users


@app.get("/users/{user_id}", response_model=schemas.User)
def read_user(user_id: int, db: Session = Depends(get_db)):
    db_user = crud.get_user(db, user_id=user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user


@app.post("/users/{user_id}/items/", response_model=schemas.Item)
def create_item_for_user(user_id: int, item: schemas.ItemCreate, db: Session = Depends(get_db)):
    return crud.create_user_item(db=db, item=item, user_id=user_id)


@app.get("/items/", response_model=list[schemas.Item])
def read_items(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    items = crud.get_items(db, skip=skip, limit=limit)
    return items


@app.post("/projects/", response_model=dict[str, schemas.Commit])
def get_project(repository: schemas.Repository, db: Session = Depends(get_db)):
    return {
        "prev-commit": {
            "message": "text: This is a test commit",
            "id": "d52feab983da8cf07ffc1c875106e0e73d5b2b95",
            "files": [
                {
                    "name": "hello-world.c",
                    "content": '#include <stdio.h>\n\nint main() {\n  printf("hello, world");\n}\n',
                }
            ],
        },
        "progress-commit": {
            "message": "text: This is a test commit",
            "id": "d52feab983da8cf07ffc1c875106e0e73d5b2b96",
            "files": [
                {
                    "name": "hello-world.c",
                    "content": '#include <stdio.h>\n\nint main() {\n  printf("hello, world\\");\n}\n',
                }
            ],
        },
        "target-commit": {
            "message": "text: This is a test commit",
            "id": "d52feab983da8cf07ffc1c875106e0e73d5b2b97",
            "files": [
                {
                    "name": "hello-world.c",
                    "content": '#include <stdio.h>\n\nint main() {\n  printf("hello, world\\n");\n}\n',
                }
            ],
        },
    }
