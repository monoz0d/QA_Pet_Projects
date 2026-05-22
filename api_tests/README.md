# API Tests - JSONPlaceholder

Проект содержит ручное и автоматизированное тестирование REST API
[JSONPlaceholder](https://jsonplaceholder.typicode.com).

JSONPlaceholder - публичный демо-API для практики тестирования.
Поддерживает GET, POST, PUT, PATCH, DELETE запросы.

## Тестируемые эндпоинты

| Метод   | URL                   | Описание                         |
|---------|-----------------------|----------------------------------|
| GET     | /users                | Получить всех пользователей      |
| GET     | /users/{id}           | Получить пользователя по ID      |
| GET     | /users/999            | Негативный тест: 404             |
| POST    | /users                | Создать пользователя             |
| PUT     | /users/{id}           | Обновить пользователя            |
| DELETE  | /users/{id}           | Удалить пользователя             |
| GET     | /posts                | Получить все посты               |
| GET     | /posts?userId=1       | Получить посты пользователя      |
| GET     | /todos?completed=true | Получить выполненные задачи      |

## Postman коллекция

Коллекция находится в папке `postman/`.

### Как импортировать в Postman:
1. Открыть Postman
2. File → Import
3. Выбрать файл `jsonplaceholder_collection.json`
4. Импортировать окружение: `jsonplaceholder_environment.json`
5. Выбрать окружение `JSONPlaceholder` в правом верхнем углу

## Автотесты (pytest + requests)

### Что покрыто

| Класс           | Метод                   | Тестов                       |
|-----------------|-------------------------|------------------------------|
| TestGetUsers    | GET /users, /users/{id} | 9                            |
| TestPostUsers   | POST /users             | 3                            |
| TestPutUsers    | PUT /users/{id}         | 2                            |
| TestDeleteUsers | DELETE /users/{id}      | 2                            |
| TestGetPosts    | GET /posts              | 4                            |
| TestGetTodos    | GET /todos              | 2                            |
| **Итого**       |                         | **22 + 4 параметризованных** |

### Результат последнего прогона
- Всего тестов: 26
- Пройдено: 26
- Провалено: 0
- Время: 29.17 секунд

### Запуск

```bash
pytest api_tests/tests/test_jsonplaceholder.py -v
```

## Установка зависимостей:

```bash
pip install -r requirements.txt
```

## Стек
- Postman (ручное тестирование API)
- Python + pytest + requests (автоматизация)