from bank import value
import pytest
def main():
    test_value()

def test_value():
    assert value("hi")==20
    assert value("adil")==100
    assert value("hello")==0
    assert value("Hari")==20
    assert value("Hello")==0


if __name__=="__main__":
    main()
