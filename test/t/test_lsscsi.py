import pytest


class TestLsscsi:

    @pytest.mark.complete("lsscsi ")
    def test_1(self, completion):
        assert not completion.list

    @pytest.mark.complete("lsscsi -")
    def test_2(self, completion):
        assert completion.list
