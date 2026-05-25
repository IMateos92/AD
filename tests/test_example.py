"""Tests para el módulo example."""

import pytest
from src.example import hello, add


class TestHello:
    """Tests para la función hello."""

    def test_hello_basic(self):
        """Test básico de la función hello."""
        assert hello("mundo") == "Hola, mundo!"

    def test_hello_with_name(self):
        """Test con diferentes nombres."""
        assert hello("Python") == "Hola, Python!"


class TestAdd:
    """Tests para la función add."""

    def test_add_positive_numbers(self):
        """Test suma de números positivos."""
        assert add(2, 3) == 5

    def test_add_negative_numbers(self):
        """Test suma de números negativos."""
        assert add(-2, -3) == -5

    def test_add_mixed_numbers(self):
        """Test suma de números mixtos."""
        assert add(-2, 3) == 1
