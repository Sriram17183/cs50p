from project import is_userlogic,battinglogic,bowlinglogic,chaselogic,tosslogic
import pytest
def test_is_userlogic():
    assert is_userlogic("even", 2, 2) is True
    assert is_userlogic("odd", 3, 2) is True
    assert is_userlogic("even", 1, 2) is False



def test_battinglogic():
    score, out = battinglogic(0, 3, 3)
    assert out is True
    assert score == 0

    score, out = battinglogic(0, 0, 4)
    assert score == 4

def test_bowlinglogic():
    score, out = bowlinglogic(0, 3, 3)
    assert out is True
    assert score == 0

    score, out = bowlinglogic(0, 2, 0)
    assert out is False
    assert score == 2

    score, out = bowlinglogic(5, 1, 4)
    assert score == 9

def test_chaselogic():
    assert chaselogic(6, 5) is True
    assert chaselogic(5, 5) is False

def test_tosslogic():
    assert tosslogic("even", 4) is True
    assert tosslogic("odd", 5) is True
    assert tosslogic("even", 3) is False


