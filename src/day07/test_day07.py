import pytest
from day07 import part1, part2

@pytest.mark.benchmark(group="day07")
def test_part1(benchmark):
    res = benchmark(part1)
    assert res == 1430271835320

@pytest.mark.benchmark(group="day07")
def test_part2(benchmark):
    res = benchmark(part2)
    assert res == 456565678667482