import pytest
from twttr  import shorten

def main():
    test_twitter()
    test_consonats()
    test_numbers()
    test_lowercase()
    test_capitalized()
def test_vowels():
    assert shorten("johny")=="jhny"
    assert shorten("HELLO")=="HLL"

def test_consonats():
    assert shorten("bcdrt")=="bcdrt"
def test_numbers():
    assert shorten("k34j")=="k34j"

def test_lowercase():
    assert shorten("lk!")=="lk!"

def test_capitalized():
    assert shorten("Karthi")=="Krth"



if __name__=="__main__":
    main()
