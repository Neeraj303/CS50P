from plates import is_valid


def test_plate_length():
    assert is_valid("HELLO") == True
    assert is_valid("H") == False
    assert is_valid("GOODBYE") == False
    assert is_valid("HI") == True

def test_plate_letter():
    assert is_valid("H100") == False
    assert is_valid("BLANK") == True
    assert is_valid("4506") == False
    assert is_valid("4RT") == False

def test_plate_number():
    assert is_valid("AAA22A") == False
    assert is_valid("BOM01A") == False
    assert is_valid("CS50") == True
    assert is_valid("CS50P") == False

def test_plate_punc():
    assert is_valid("!HII!") == False
    assert is_valid("OK.KO") == False
    assert is_valid("!HI YOU") == False
    assert is_valid("N@me") == False

def test_plate_zero():
    assert is_valid("CS50") == True
    assert is_valid("CS05") == False
    assert is_valid("ART070") == False
    assert is_valid("ART700") == True
