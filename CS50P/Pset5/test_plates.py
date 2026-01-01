import pytest
from plates import is_valid

def main():
    test_plates

def test_plates():
    assert is_valid("a123")==False
    assert is_valid("cs50")==True
    assert is_valid("alphabet")==False
    assert is_valid("alpha0")==False
    assert is_valid("1cat")==False
    assert is_valid("cs50p")==False
    assert is_valid("cs50@")==False
if __name__=="__main__":
    main()
