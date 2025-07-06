from numb3rs import validate



def main():
    test_format1()
    test_format2()
    test_format3()

def test_format1():
    assert validate("2.3.45.5")==True
    assert validate("2.43.45.5")==True
    assert validate("24.3.45.55")==True

def test_format2():
    assert validate("2.3.545.5")==False
    assert validate("2.43.745.5")==False
    assert validate("24.376.45.55")==False

def test_format3():
    assert validate("2.354.5")==False
    assert validate("2.vsd.5")==False
    assert validate("24.bf.45.55")==False


if __name__ == "__main__":
    main()
