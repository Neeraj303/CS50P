from jar import Jar
import pytest


def test_init():
    jar = Jar()
    assert jar.capacity == 12
    assert jar.size == 0

    jar = Jar(10, 4)
    assert jar.capacity == 10
    assert jar.size == 4

def test_str():
    jar = Jar()
    assert str(jar) == ""
    jar.deposit(1)
    assert str(jar) == "🍪"
    jar.deposit(11)
    assert str(jar) == "🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪"


def test_deposit():
    jar = Jar(10,5)
    jar.deposit(3)
    assert jar.size == 8

    with pytest.raises(ValueError):
        jar.deposit(3)

def test_withdraw():
    jar = Jar(10, 4)
    jar.withdraw(2)
    assert jar.size == 2

    with pytest.raises(ValueError):
        jar.withdraw(3)
