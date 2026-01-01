import pytest
from working import convert

def main():
    test_working()
    test_invalid()

def test_working():
    assert convert("9 AM to 5 PM")=="09:00 to 17:00"
    assert convert("9:00 AM to 5 PM")== "09:00 to 17:00"
    assert convert("1:00 PM to 5:00 PM")=="13:00 to 17:00"
    assert convert("12:01 PM to 1:01 PM")=="12:01 to 13:01"

def test_invalid():
    with pytest.raises (ValueError):
        convert("9:60 AM TO 5:70 PM")
    with pytest.raises (ValueError):
        convert("9AM to 5PM")
    with pytest.raises(ValueError):
        convert(" 9 AM  5 PM")
    with pytest.raises(ValueError):
        convert("123 AM to 570 PM")



if __name__=="__main__":
    main()


