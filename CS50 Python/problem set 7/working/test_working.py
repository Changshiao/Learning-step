from working import convert
import pytest

def test_working():
    test_working1()
    test_working2()
    test_working3()
    test_working4()



def test_working1():
    with pytest.raises(ValueError):
        convert('cat AM to 5:00 PM')
def test_working2():
    with pytest.raises(ValueError):
        convert('12:71 AM to 5:00 PM')
def test_working3():
    assert (convert('9:00 AM to 5:00 PM')=='09:00 to 17:00')

def test_working4():
    with pytest.raises(ValueError):
        convert('12:71 AM  5:00 PM')


def main():
    test_working()

if __name__ == "__main__":
    main()
