import pytest


def test_filename():
    with pytest.raises(IOError):
        open("12345.txt", "r") # файла не должно быть в директории
