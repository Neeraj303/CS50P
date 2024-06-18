from twttr import shorten

def test__small_shorten():
    assert shorten("twitter") == "twttr"
    assert shorten("hello") == "hll"
    assert shorten("goodbye") == "gdby"

def test_cap_shorten():
    assert shorten("APPLE") == "PPL"
    assert shorten("CS50") == "CS50"

def test_int_shorten():
    assert shorten("hello12") == "hll12"
    assert shorten("GREAT69") == "GRT69"

def test_punc_shorten():
    assert shorten("hello!") == "hll!"
    assert shorten("What ?") == "Wht ?"
