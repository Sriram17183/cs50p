from CS50P.fuel import convert,gauge
import pytest

def main():
    test_convert()
    test_gauge()

def test_convert():
    assert convert("1/2") == 50
    assert convert("3/4") == 75
    assert convert("1/100") == 1

def test_invalid():
    with pytest.raises (ValueError):
        convert("cat/dog")
    with pytest.raises (ValueError):
        convert("-5/3")
    with pytest.raises(ZeroDivisionError):
        convert("2/0")


def test_gauge():
    assert gauge(99)=="F"
    assert gauge(100)=="F"
    assert gauge(50)=="50%"
    assert gauge(0)=="E"
    assert gauge(1)=="E"


if __name__=="__main__":
    main()
