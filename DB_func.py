from DB import engine
from models import Questions,create_table
from sqlalchemy.orm import Session
from jservice_api import get_question
session = Session(bind=engine)

def add_question(question:str,question_id:int,answer:str,created_at:str,category_id:int):
    """Добавляем вопрос в базу данных если он прошел валидацию"""
    valid=question_validation(question_id,category_id)
    if valid==True:
        qu=Questions(
            question=question,
            question_id=question_id,
            answer=answer,
            created_at=created_at,
            category_id=category_id
        )
        session.add(qu)
        session.commit()
    else:
       qu = get_question(1)
       qu=qu[0]
       print(qu)
       add_question(question=qu['question'], question_id=qu['id'], answer=qu["answer"],
                    created_at=qu["created_at"], category_id=qu["category_id"])

def question_validation(question_id:int,category_id:int):
    validation_data=session.query(Questions).filter(Questions.question_id==question_id,Questions.category_id==category_id).all()
    if validation_data:
        return False
    return True

def get_last_one_question():
    how_many_q = session.query(Questions).count()
    if how_many_q>0:
        print(how_many_q)
        last_one_question=session.get(Questions,how_many_q)
        return last_one_question.question
    else:
        return None
