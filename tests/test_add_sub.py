import pytest
from src.main import add, sub


@pytest.mark.parametrize(
    ('a', 'b', 'c'), [
        (1, 2, 3),
        (2, 3, 5),
        (3, 4, 7),
    ]
)
def test_add(a, b, c):
    assert add(a, b) == c


@pytest.mark.parametrize(
    ('a', 'b', 'c'), [
        (3, 2, 1),
        (5, 3, 2),
        (7, 4, 3),
    ]
)
def test_sub(a, b, c):
    assert sub(a, b) == c
