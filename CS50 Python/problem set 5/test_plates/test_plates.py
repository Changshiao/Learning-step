from plates import is_valid


def main():
    test_valid1()
    test_valid2()
    test_valid3()


def test_valid1():
    assert is_valid("HELLO")==True
    assert is_valid("HE345")==True
def test_valid2():
    assert is_valid("CS50a")==False
    assert is_valid("CS05")==False
    assert is_valid("uiewoiruo")==False
    assert is_valid("05uie")==False
def test_valid3():
    assert is_valid("fj,4")==False
    assert is_valid("g")==False

if __name__=="__main__":
    main()
