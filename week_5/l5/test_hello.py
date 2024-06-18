from hello import hello

def main():
    test_arg()

def test_arg():
    assert hello('Neeraj') == "hello, Neeraj"

def test_default():
    assert hello() == "hello, world"

if __name__ == "__main__":
    main()