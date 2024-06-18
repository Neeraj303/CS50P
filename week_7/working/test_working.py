from working import convert
import pytest

def test_normal_correct():
    assert convert("9:00 AM to 5:00 PM") == "09:00 to 17:00"
    assert convert("9 AM to 5 PM") == "09:00 to 17:00"
    assert convert("9 PM to 5:30 AM") == "21:00 to 05:30"

def test_incorrect():
    with pytest.raises(ValueError):
        convert("9:00 AM - 5:00 PM")

    with pytest.raises(ValueError):
        convert("13 AM to 5 PM")

    with pytest.raises(ValueError):
        convert("9 AM to 13 PM")



