import pytest


class TestArping:

    @pytest.mark.complete("arping ")
    def test_1(self, completion):
        assert completion.list

    @pytest.mark.complete("arping -")
    def test_2(self, completion):
        assert completion.list
