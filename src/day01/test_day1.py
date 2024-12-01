import pytest
import day1

@pytest.mark.benchmark(group="day01")
def test_part1(benchmark):
    res = benchmark(day1.part1)
    assert res == 1590491

@pytest.mark.benchmark(group="day01")
def test_part2(benchmark):
    res = benchmark(day1.part2)
    assert res == 22588371