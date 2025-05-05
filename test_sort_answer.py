import pytest
from sort_answer import sort


def test_sort_works():
    assert sort(1, 1, 1, 1)


def test_sort_special():
    assert sort(150, 1, 1, 1) == "SPECIAL"
    assert sort(1, 150, 1, 1) == "SPECIAL"
    assert sort(1, 1, 150, 1) == "SPECIAL"
    assert sort(1_000_000, 1, 1, 1) == "SPECIAL"
    assert sort(1, 1, 1, 20) == "SPECIAL"


def test_sort_rejected():
    assert sort(150, 1, 1, 1_000_000) == "REJECTED"
