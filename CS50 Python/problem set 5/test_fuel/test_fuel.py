import pytest
from fuel import convert
from fuel import gauge


def main():
    test_errors()
    test_percentages()
    test_value()


def test_errors():
    with pytest.raises(ValueError):
        convert("cat/dog")
def test_value():
    with pytest.raises(ZeroDivisionError):
        convert("1/0")

def test_percentages():
    assert convert('1/4')==25 and gauge(25) == "25%"
    assert gauge(convert('1/100'))=='E'
    assert gauge(convert('99/100')) == "F"

if __name__ == "__main__":
    main()
