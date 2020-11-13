import pytest
from main import enter_password

#password is less than 6  - not accepted (False)
def test_1():
    assert enter_password('as') is False

# password is more than 6 - accepted True
def test_2():
    assert enter_password('asdfgteuej767') is True
