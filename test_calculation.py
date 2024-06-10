import pytest
from main import calculation

def test_calc():
    calc = calculation([1, 2, 3, 4, 5])
    assert calc.get_sum() == 15

    calc = calculation([0, 0, 0, 0])
    assert calc.get_sum() == 0
    
    calc = calculation([-1, 1, -1, 1])
    assert calc.get_sum() == 0