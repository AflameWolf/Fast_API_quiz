from sqlalchemy import (Integer,String, Column)
from sqlalchemy.orm import declarative_base

from DB import engine

Base = declarative_base()

class Questions(Base):
    __tablename__ = 'Questions'
    id = Column(Integer, primary_key=True)
    question = Column(String, nullable=False)
    question_id = Column(Integer, nullable=False)
    answer = Column(String, nullable=False)
    created_at = Column(String, nullable=False, unique=True)
    category_id=Column(Integer, nullable=False)


def create_table(engine=engine):
    Base.metadata.create_all(engine)
    return

