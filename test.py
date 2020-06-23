from assertive_programming import text_to_morsecode
from assertive_programming import morsecode_to_text

import pytest

def test_text_to_morsecode():
    assert text_to_morsecode("Hi There") == " - .... . .-. . "

def test_morsecode_to_text():
    assert morsecode_to_text(".... .. / - .... . .-. .")== "HI THERE"