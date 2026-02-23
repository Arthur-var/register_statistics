from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from app import models, schemas
from app.database import engine, SessionLocal, Base

app = FastAPI()

Base.metadata.create_all(bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

#@app.post("/reg")
@app.post("/register")
def register(user: schemas.UserCreate, db: Session = Depends(get_db)):
    db_user = models.User(username=user.username)
    db.add(db_user)
    db.commit()
    return {"message": "User created"}

@app.post("/tasks")
def create_task(task: schemas.TaskCreate, user_id: int, db: Session = Depends(get_db)):
    db_task = models.Task(title=task.title, user_id=user_id)
    db.add(db_task)
    db.commit()
    return {"message": "Task created"}

@app.get("/tasks", response_model=list[schemas.TaskOut])
def get_tasks(user_id: int, db: Session = Depends(get_db)):
    return db.query(models.Task).filter(models.Task.user_id == user_id).all()
    #return db.query(models.Task)