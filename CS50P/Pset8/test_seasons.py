from seasons import Time
import pytest
def main():
    test_seasons()

def test_seasons():
    d = "1981-11-02"
    dob = Time(d)
    assert dob.minutes_lived()==2,32,22,880

if __name__=="__main__":
    main()
