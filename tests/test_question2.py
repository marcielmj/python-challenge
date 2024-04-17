import pytest

from python_challenge.question2 import Orders


@pytest.mark.parametrize(
    ("requests", "n_max", "expected"),
    [
        ([70, 30, 10], 100, 2),
        ([50, 50, 50, 50, 50], 100, 3),
        ([1000, 2000, 3000, 4000], 5000, 2),
        ([2000, 2000, 2000, 2000, 2000], 4000, 3),
        ([1000, 2000, 3000, 4000, 5000], 6000, 3),
        ([1000, 2000, 3000, 4000, 5000, 6000], 7000, 3),
        ([1000, 2000, 3000, 4000, 5000, 6000, 7000], 8000, 4),
    ],
)
def test_combine_orders(requests, n_max, expected):
    orders = Orders()
    assert orders.combine_orders(requests, n_max) == expected
