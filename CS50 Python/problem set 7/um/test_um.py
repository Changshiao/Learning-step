import pytest
from um import count

def main():
    test_count()

def test_count():
    assert count('um...  ')==1
    assert count('yummy')==0
    assert count('y,um...my.um,what')==2
    assert count('uM')==1
    assert count('1512asdf51243')==0

if __name__ == "__main__":
    main()
