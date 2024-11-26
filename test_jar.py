import pytest #я добавил

from jar import Jar

def test_initial_capacity():
    jar = Jar(10)
    assert jar.capacity == 10

def test_default_capacity():
    jar = Jar()
    assert jar.capacity == 12

def test_deposit_within_capacity():
    jar = Jar(5)
    jar.deposit(3)
    assert jar.size == 3

def test_withdraw_within_capacity():
    jar = Jar(5)
    jar.deposit(3)
    jar.withdraw(2)
    assert jar.size == 2

#добавьте проверки исключений. Например:
def test_capacity_positive():
    jar = Jar()
    with pytest.raise(ValueError):
        jar.capacity = -10



