import pytest  # pip install pytest

from PyTest_examples.code_pytest import sumuj, dajCyfry, is_palindrome, getOne, getData, loadDB, calculate_average, calculate_percentage


def test_sumuj():
    assert sumuj(5, 3) == 8


def test_dajCyfryMin():
    tab = dajCyfry()
    assert min(tab) == 1


def test_dajCyfryMax():
    tab = dajCyfry()
    assert max(tab) == 10


def test_dajCyfryLen():
    tab = dajCyfry()
    assert len(tab) == 10


def test_palindrome_true():
    assert is_palindrome("kajak") == True
    assert is_palindrome("kajak           ") == True
    assert is_palindrome("level") == True
    assert is_palindrome("A man a plan a canal Panama") == True
    assert is_palindrome("racecar") == True


lista_przypadkow_testowych = ["hello", "python", "123456x"]


@pytest.mark.parametrize('text', lista_przypadkow_testowych)
def test_palindrome_false(text):
    assert is_palindrome(text) == False


lista_przypadkow_testowych2 = [("hello", False), ("python", False), ("123456x", False)]


@pytest.mark.parametrize('text, result', lista_przypadkow_testowych2)
def test_palindrome_false_parametryzacja_z_wynikiem(text, result):
    assert is_palindrome(text) == result


def test_palindrome_empty_true():
    assert is_palindrome("") == True


def test_average_empty_list():
    assert calculate_average([]) is None


@pytest.mark.parametrize("numbers, expected_result", [
    ([1, 2, 3], 2.0),
    ([0, 0, 0, 0], 0.0),
    ([10, 20, 30, 40, 50], 30.0),
])
def test_average_parametrized(numbers, expected_result):
    assert calculate_average(numbers) == expected_result


# def setup_module():
#     print("\n############## setup ##############")
#     loadDB()
# def teardown_module():
#     print("\n############## bye ##############")
#
# def test_getOne():
#     assert getOne(0)[1]=='Marian'
#
# def test_getData():
#     assert len(getData()) > 0

@pytest.fixture(scope="module", autouse=True)
def setup_and_teardown():
    print("\n############## setup ##############")
    loadDB()
    yield
    print("\n############## bye ##############")


def test_getData():
    assert len(getData()) > 0


def test_getOne():
    assert getOne(0)[1] == 'Marian'


# @pytest.fixture(autouse=True)
# def load_stuff():
#     print("\n############## load ##############")
#     loadDB()
#
# def test_getData_1():
#     assert len(getData()) > 0
#
# def test_getOne_1():
#     assert getOne(0)[1] == 'Marian'


# def test_calculate_percentage_valid_percent():
#     assert calculate_percentage(100, 50) == 50.0
#     assert calculate_percentage(200, 25) == 50.0

def test_calculate_percentage_invalid_percent():
    with pytest.raises(ValueError) as e:
        calculate_percentage(100, -10)
    assert str(e.value) == "Percent must be between 0 and 100"





