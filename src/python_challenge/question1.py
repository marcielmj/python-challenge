class Contract:
    def __init__(self, id, debt):
        self.id = id
        self.debt = debt

    def __str__(self):
        return f'id={self.id}, debt={self.debt}'


class Contracts:
    def get_top_N_open_contracts(self, open_contracts: list[Contract], renegotiated_contracts: list[int], top_n: int) -> list[int]:
        """
        Returns the top N debtors who have not renegotiated their debts.

        Parameters:
        open_contracts (List[Contract]): A list representing the outstanding financial operations of each associate.
        renegotiated_contracts (List[int]): A list representing the identifiers of associates who have already renegotiated their debts.
        top_n (int): The number of debtors to be returned by the method.

        Returns:
        List[int]: A list containing the identifiers of the top N debtors, sorted from the highest debtor to the lowest.
        The position 0 will have the highest debtor, and the position top_n - 1 will have the lowest debtor.
        """
        sorted_open_contracts = sorted(open_contracts, key=lambda x: x.debt, reverse=True)
        debts = [contract.id for contract in sorted_open_contracts if contract.id not in renegotiated_contracts]

        if top_n == -1:
            return [debts.pop()]

        return debts[:top_n]
