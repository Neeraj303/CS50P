from bank import value

def test_hello_value():
    assert value('hello, aman') == 0
    assert value('HELLO, ND') == 0
    assert value('hello') == 0

def test_h_value():
    assert value('hi, sir') == 20
    assert value('hey, how are you') == 20
    assert value('hiii') == 20
    assert value('how are you') == 20

def test_noh_value():
    assert value('kaisa hai bhai') == 100
    assert value('aur londe kaisa hai') == 100
    assert value('what\'s up') == 100

