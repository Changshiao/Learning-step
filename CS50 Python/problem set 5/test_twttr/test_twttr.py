from twttr import shorten

def main():
    text_twttr1()
    text_twttr2()
    text_twttr3()



def test_twttr1():
    assert shorten("TweE")=="Tw"

def test_twttr2():
    assert shorten("?")=="?"

def test_twttr3():
    assert shorten("12")=="12"



if __name__ == "__main__":
    main()
