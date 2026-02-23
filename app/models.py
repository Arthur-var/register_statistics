from sqlalchemy import Column, Integer, String, ForeignKey
from app.database import Base

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)


class Task(Base):
    __tablename__ = "tasks"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    status = Column(String, default="new")
    user_id = Column(Integer, ForeignKey("users.id"))


'''
class Solve(Base):
    __tablename__ = "solve"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    kira = Column(String, default="new")
'''