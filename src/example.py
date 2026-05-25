"""
Módulo de ejemplo.

Este módulo contiene funciones de ejemplo que se documentarán automáticamente
usando mkdocstrings.
"""


def hello(name: str) -> str:
    """
    Retorna un saludo personalizado.

    Args:
        name: El nombre de la persona a saludar.

    Returns:
        Un string con el saludo.

    Example:
        >>> hello("mundo")
        'Hola, mundo!'
    """
    return f"Hola, {name}!"


def add(a: int, b: int) -> int:
    """
    Suma dos números.

    Args:
        a: El primer número.
        b: El segundo número.

    Returns:
        La suma de a y b.

    Example:
        >>> add(2, 3)
        5
    """
    return a + b
