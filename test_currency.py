
from student import inr_to_usd

def test_inr_to_usd():
    assert inr_to_usd(9800) == 100.00

def test_small_amount():
    assert inr_to_usd(490) == 5.00

def test_zero_amount():
    assert inr_to_usd(0) == 0.00
