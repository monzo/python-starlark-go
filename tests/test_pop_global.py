import pytest

from starlark_go import Starlark


def test_pop_global():
    s = Starlark(globals={"a": 1, "b": 2, "c": 3})

    assert sorted(s.globals()) == ["a", "b", "c", "struct"]

    b = s.pop("b")

    assert b == 2
    assert sorted(s.globals()) == ["a", "c", "struct"]

    with pytest.raises(KeyError):
        s.pop("b")

    assert s.pop("b", None) is None

    assert sorted(s.globals()) == ["a", "c", "struct"]
