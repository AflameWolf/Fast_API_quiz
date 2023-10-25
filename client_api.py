from fastapi import FastAPI
from DB_func import add_question,get_last_one_question
from jservice_api import get_question
from models import create_table
app=FastAPI(title="newapp")



@app.post("/question/")
def question_api(quantity:int):
    """Принимаем количество вопросов """

    questions=get_question(quantity)
    return_question=get_last_one_question()
    for i in questions:
        add_question(question=i['question'],question_id= i['id'], answer=i["answer"],
                         created_at=i["created_at"], category_id=i["category_id"])

    return {"status":200,"question":return_question}



