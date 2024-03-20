import time
import pytest

@pytest.mark.podstawowe
def test_inny():
    assert 4 == 4

@pytest.mark.podstawowe
def test_true():
    assert True

@pytest.mark.zaawansowane
def test_czy_to_dziala():
    assert 1 == 2


@pytest.mark.bardzo_wolne
def test_ktory_potrzebuje_czasu():
    time.sleep(5)
    assert 1 == 1
