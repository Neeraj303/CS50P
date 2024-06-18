from um import count

def test_no_um():
    assert count("Kikar ho sa") == 0
    assert count("How are you") == 0
    assert count("I need that") == 0

def test_incorrect_um():
    assert count("Yummy food") == 0
    assert count("Umang is great") == 0
    assert count("hum toh jaa rahe hai") == 0

def test_correct_um():
    assert count("Um, the food is good") == 1
    assert count("um..., I guess, um...") == 2
    assert count(" um ") == 1

