# Fast api for quizzes

Приложение для демонстрации работы с Docker и Docker compose.

При запросе получает указанное колличество вопросов, используя API https://jservice.io.
Сохраняет их в базу данных и возвращает последний вопрос из сохраненных при предыдущем обращении.
____
## Используемые технологии:
  + Fast_api
  + SQlalchemy
  + PostgreSQL
  + Docker
  + Docker Compose
____
## Установка
1. Установите Docker и Docker Compose 
2. Клонируйте репозиторий
3. В файле docker-compose настройте порты
    + При необходимости настройте `POSTGRES_PASSWORD` и `POSTGRES_USER`. 
    + **Не забудьте так же внести изменения в окружение .env!**
4. Запустите команду `docker compose up` и дождитесь развертывания

____
При первом запуске для создания таблицы в базе данных используйте:
```
docker exec fast_api_app python -c 'import models; models.create_table()'
```
___
## Использование:
Отправте POST запрос `http://localhost:Ваш порт/question/?quantity=количество вопросов` используя Postman или `http://localhost:ваш порт/docs`.
