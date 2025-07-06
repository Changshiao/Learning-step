from bank import value


def main():
    test_bank_0()
    test_bank_20()
    test_bank_100()

def test_bank_0():
    assert value('Hello ji')==0
    assert value("hELLO")==0


def test_bank_20():
    assert value("Hi ji ")==20
    assert value("hi")==20
    assert value("Hei")==20

def test_bank_100():
    assert value("ko")==100
    assert value("where are you")==100

if __name__=="__main__":
    main()
