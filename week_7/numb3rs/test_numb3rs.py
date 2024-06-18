from numb3rs import validate

def test_correct_validate():
    assert validate("127.0.0.1") == True
    assert validate("255.255.255.0") == True
    assert validate("0.3.5.26") == True
    assert validate("0.0.0.0") == True

def test_incorrect_validate():
    assert validate("cat") == False
    assert validate("1.cat.4.65") == False
    assert validate("265.3.4.5") == False
    assert validate("546.34.23.67") == False

def test_first_validate():
    assert validate("26.565.45.7") == False
    assert validate("456.34.135.5") == False
    assert validate("984.45.67.53") == False
    assert validate("1000.1.13.1") == False
