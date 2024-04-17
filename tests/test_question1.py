import pytest

from python_challenge.question1 import Contract, Contracts


@pytest.mark.parametrize(
    ("open_contracts", "renegotiated", "top_n", "expected"),
    [
        ([Contract(1, 1), Contract(2, 2), Contract(3, 3), Contract(4, 4), Contract(5, 5)], [3], 3, [5, 4, 2]),
        ([Contract(1, 5000), Contract(2, 4000), Contract(3, 6000), Contract(4, 2000), Contract(5, 3000)], [2, 4], 3, [3, 1, 5]),
        ([Contract(1, 5000), Contract(2, 4000), Contract(3, 6000), Contract(4, 2000), Contract(5, 3000), Contract(6, 7000)], [2, 4, 6], 2, [3, 1]),
        ([Contract(1, 5000), Contract(2, 4000), Contract(3, 6000), Contract(4, 2000), Contract(5, 3000), Contract(6, 7000), Contract(7, 8000)], [2, 4, 6, 7], 1, [3]),
        ([Contract(1, 5000), Contract(2, 4000), Contract(3, 6000), Contract(4, 2000), Contract(5, 3000), Contract(6, 7000), Contract(7, 8000)], [2, 6, 7], -1, [4]),
    ]
)
def test_get_top_n_open_contracts(open_contracts, renegotiated, top_n, expected):
    contracts = Contracts()
    result = contracts.get_top_N_open_contracts(open_contracts, renegotiated, top_n)
    assert result == expected
