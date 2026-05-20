import pytest
import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from safe_password_generator import generate_password, verify
class TestPasswordGenerator:
    """Тесты для функции generate_password"""
    def test_password_has_correct_length(self):
        """Пароль должен иметь длину, которую мы указали."""
        password = generate_password(8, '0123456789')
        assert len(password) == 8
    def test_password_contains_only_digits(self):
        """Если передали только цифры - в пароле только цифры"""
        chars = '0123456789'
        password = generate_password(10, chars)
        for char in password:
            assert char in chars
    def test_password_contains_only_lowercase(self):
        """Если передали только строчные буквы - в пароле только строчные"""
        chars = 'abcdefghijklmnopqrstuvwxyz'
        password = generate_password(10, chars)
        for char in password:
            assert char in chars
    def test_password_contains_only_uppercase(self):
        """Если передали только прописные буквы - в пароле только просписные"""
        chars = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        password = generate_password(10, chars)
        for char in password:
            assert char in chars
    def test_password_length_1(self):
        """Граничный случай: минимальная длина пароля - 1"""
        password = generate_password(1, 'abc')
        assert len(password) == 1
    def test_password_length_100(self):
        """Граничный случай: максимальная длина пароля - 100"""
        password = generate_password(100, 'abc')
        assert len(password) == 100
    def test_empty_chars_raises_error(self):
        """Пустой набор символов вызывает Index Error"""
        with pytest.raises(IndexError):
            generate_password(8, '')
    def test_password_is_string(self):
        """Результат должен быть строкой"""
        password = generate_password(8, '0123456789')
        assert isinstance(password, str)
    @pytest.mark.parametrize('length', [1,5,8,16,32,100])
    def test_various_lengths(self, length):
        """Параметризованный тест: пароль правильной длины при разных значениях"""
        password = generate_password(length, 'abc123')
        assert len(password) == length
    @pytest.mark.parametrize('chars', ['0123456789', 'abcdefghijklmnopqrstuvwxyz', 'ABCDEFGHIJKLMNOPQRSTUVWXYZ', '!#$%&*+-=?@^_'])
    def test_various_chars(self, chars):
        """Параметризованный тест: пароль содержит только символы из набора"""
        password = generate_password(15, chars)
        for char in password:
            assert char in chars
class TestVerify:
    """Тесты для функции verify"""
    def test_yes_returns_chars(self):
        """Ответ 'да' должен возвращать переданные символы"""
        result = verify('да', '0123456789')
        assert result == '0123456789'
    def test_uppercase_yes(self):
        """'ДА' должно работать так же, как 'да'"""
        result = verify('ДА', '0123456789')
        assert result == '0123456789'

    def test_uppercase_no(self):
        """'НЕТ' должно работать так же, как 'нет'"""
        result = verify('НЕТ', 'abc')
        assert result == ''
    def test_yes_with_empty_chars(self):
        """Если набор символов пуст и ответ 'да', то возвращается пустая строка"""
        result = verify('да', '')
        assert result == ''
    @pytest.mark.parametrize('answer,chars,expected', [('да', '0123456789', '0123456789'), ('нет', '0123456789', ''), ('да', 'abc', 'abc'), ('нет', 'abc', '')])
    def test_parametrized_verify(self, answer, chars, expected):
        """Параметризованный тест: разные комбинации ответов и символов"""
        result = verify(answer, chars)
        assert result == expected