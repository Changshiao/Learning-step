from seasons import get_time


def test_get_time():
    assert get_time('1245-09-02')==('1245','09','02')
    assert get_time('1245-09-32')==False
    assert get_time('1245-july-12')==False

def main():
    test_get_time()


if __name__ == "__main__":
    main()
