import requests
import pytest
base_url = 'https://jsonplaceholder.typicode.com'
class TestGetUsers:
    """Тесты для GET запросов к ресурсу Users"""
    def test_get_users_status_code(self):
        """Статус-код при получении всех пользователей должен быть 200 OK"""
        response = requests.get(f'{base_url}/users')
        assert response.status_code == 200
    def test_get_all_users_returns_list(self):
        """Ответ должен быть списком"""
        response = requests.get(f'{base_url}/users')
        assert isinstance(response.json(), list)
    def test_get_all_users_count(self):
        """Список должен содержать 10 пользователей."""
        response = requests.get(f'{base_url}/users')
        assert len(response.json()) == 10
    def test_get_user_by_id_status_code(self):
        """Статус-код при получении пользователя по ID должен быть 200."""
        response = requests.get(f'{base_url}/users/1')
        assert response.status_code == 200
    def test_get_user_by_id_returns_correct_id(self):
        """Возвращенный пользователь должен иметь правильный ID."""
        response = requests.get(f'{base_url}/users/1')
        data = response.json()
        assert data['id'] == 1
    def test_get_user_has_required_fields(self):
        """Пользователь должен содержать обязательные поля."""
        response = requests.get(f'{base_url}/users/1')
        data = response.json()
        assert 'id' in data
        assert 'name' in data
        assert 'email' in data
        assert 'username' in data
    def test_get_nonexistent_user_status_code(self):
        """Запрос несуществующего пользователя должен вернуть 404."""
        response = requests.get(f'{base_url}/users/999')
        assert response.status_code == 404
    def test_response_is_json(self):
        """Ответ должен быть в формате JSON."""
        response = requests.get(f'{base_url}/users/1')
        assert response.headers['Content-Type'] == 'application/json; charset=utf-8'
    @pytest.mark.parametrize("user_id", [1, 2, 3, 4, 5])
    def test_get_multiple_users_by_id(self, user_id):
        """Параметризованный тест: каждый пользователь существует."""
        response = requests.get(f'{base_url}/users/{user_id}')
        assert response.status_code == 200
        assert response.json()['id'] == user_id
class TestPostUsers:
    """Тесты для POST запросов к ресурсу Users."""
    def test_create_user_status_code(self):
        """Статус-код при создании пользователя должен быть 201."""
        new_user = {'name': 'Никита Калашников', 'username': 'monoz0d', 'email': 'peacemaker4453@gmail.com'}
        response = requests.post(f'{base_url}/users', json=new_user)
        assert response.status_code == 201
    def test_create_user_returns_id(self):
        """Созданный пользователь должен получить ID."""
        new_user = {'name': 'Никита Калашников', 'username': 'monoz0d', 'email': 'peacemaker4453@gmail.com'}
        response = requests.post(f'{base_url}/users', json=new_user)
        data = response.json()
        assert 'id' in data
    def test_create_user_returns_correct_data(self):
        """Ответ должен содержать отправленные данные."""
        new_user = {'name': 'Никита Калашников', 'username': 'monoz0d', 'email': 'peacemaker4453@gmail.com'}
        response = requests.post(f'{base_url}/users', json=new_user)
        data = response.json()
        assert data['name'] == new_user['name']
        assert data['email'] == new_user['email']
class TestPutUsers:
    """Тесты для PUT запросов к ресурсу Users."""
    def test_update_user_status_code(self):
        """Статус-код при обновлении пользователя должен быть 200."""
        updated_user = {'id': 1, 'name': 'Никита', 'username': 'monoz0d', 'email': 'peacemaker44@mail.ru'}
        response = requests.put(f'{base_url}/users/1', json=updated_user)
        assert response.status_code == 200
    def test_update_user_returns_updated_data(self):
        """Ответ должен содержать обновленные данные."""
        updated_user = {'id': 1, 'name': 'Никита', 'username': 'monoz0d', 'email': 'peacemaker44@mail.ru'}
        response = requests.put(f'{base_url}/users/1', json=updated_user)
        data = response.json()
        assert data['name'] == 'Никита'
        assert data['email'] == 'peacemaker44@mail.ru'
class TestDeleteUsers:
    """Тесты для DELETE запросов к ресурсу Users."""
    def test_delete_user_status_code(self):
        """Статус-код при удалении пользователя должен быть 200."""
        response = requests.delete(f'{base_url}/users/1')
        assert response.status_code == 200
    def test_delete_user_returns_empty_object(self):
        """Ответ при удалении должен быть пустым объектом."""
        response = requests.delete(f'{base_url}/users/1')
        assert response.json() == {}
class TestGetPosts:
    """Тесты для GET запросов к ресурсу Posts."""
    def test_get_all_posts_status_code(self):
        """Статус-код при получении всех постов должен быть 200."""
        response = requests.get(f'{base_url}/posts')
        assert response.status_code == 200
    def test_get_all_posts_count(self):
        """Список должен содержать 100 постов."""
        response = requests.get(f'{base_url}/posts')
        assert len(response.json()) == 100
    def test_get_posts_by_user(self):
        """Фильтрация постов по userId должна работать корректно."""
        response = requests.get(f'{base_url}/posts', params={'userId': 1})
        data = response.json()
        assert len(data) == 10
        for post in data:
            assert post['userId'] == 1
    def test_post_has_required_fields(self):
        """Пост должен содержать обязательные поля."""
        response = requests.get(f'{base_url}/posts/1')
        data = response.json()
        assert 'id' in data
        assert 'title' in data
        assert 'body' in data
        assert 'userId' in data
class TestGetTodos:
    """Тесты для GET запросов к ресурсу Todos."""
    def test_get_completed_todos(self):
        """Фильтрация задач по completed=true должна работать."""
        response = requests.get(f'{base_url}/todos', params={'completed': 'true'})
        data = response.json()
        assert response.status_code == 200
        for todo in data:
            assert todo['completed'] is True
    def test_get_uncompleted_todos(self):
        """Фильтрация задач по completed=false должна работать."""
        response = requests.get(f'{base_url}/todos', params={'completed': 'false'})
        data = response.json()
        assert response.status_code == 200
        for todo in data:
            assert todo['completed'] is False