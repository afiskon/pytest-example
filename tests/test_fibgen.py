from fibgen import fibgen
import pytest


class TestFibgen:

    def test_type_error(self):
        with pytest.raises(TypeError):
            list(fibgen('ololo'))

    def test_negative(self):
        assert(list(fibgen(-1)) == [])

    def test_empty(self):
        assert(list(fibgen(0)) == [])

    def test_one(self):
        assert(list(fibgen(1)) == [1])

    def test_two(self):
        assert(list(fibgen(2)) == [1,1])

    def test_three(self):
        assert(list(fibgen(3)) == [1, 1, 2])

    def test_seven(self):
        # result = list(fibgen(10))
        result = list(fibgen(7))
        expected = [1, 1, 2, 3, 5, 8, 13]
        assert(result == expected)

    @pytest.mark.randomize(num=int, min_num=3, max_num=1000, ncalls=100)
    def test_quickcheck(self, num):
        result = list(fibgen(num))
        assert(result[0] < result[-1])
        assert(len(result) == num)