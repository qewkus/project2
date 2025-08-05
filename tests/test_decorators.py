import pytest
from src.decorators import log, my_function, my_function_1

def test_log():
    assert log()

def test_log_right(capsys):
    my_function(1, 3)
    captured = capsys.readouterr()
    assert captured.out == ''

def test_log_err():
    with pytest.raises(Exception):
        my_function(1, 'b')

def test_log_1(capsys):
    my_function_1(2, 2)
    captured = capsys.readouterr()
    assert "my_function_1 ok" in captured.out


