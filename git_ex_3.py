class BankSystem:
    def __init__(self):
        self.accounts = {}

    def account_creation(self, account_id, initial_balance=0):
        self.accounts[account_id] = initial_balance

    def balance_inquiry(self, account_id):
        return self.accounts.get(account_id, 0)

    def deposit(self, account_id, amount):
        if account_id in self.accounts:
            self.accounts[account_id] += amount

    def withdrawal(self, account_id, amount):
        if self.accounts.get(account_id, 0) >= amount:
            self.accounts[account_id] -= amount
        else:
            raise ValueError("nickel less cage")

    def account_summary(self):
        summary = ""
        for account_id, balance in self.accounts.items():
            summary += f"account ID: {account_id}, current balance: {balance}\n"
        return summary.strip()


def test():
    dude = BankSystem()
    dude.account_creation("1111", 500)

    assert dude.balance_inquiry("1111") == 500, "creation worked"
    dude.deposit("1111", 500)

    assert dude.balance_inquiry("1111") == 1000, "deposit worked"
    dude.withdrawal("1111", 300)

    assert dude.balance_inquiry("1111") == 700, "withdrawal worked"

    assert dude.balance_inquiry("12345") == 0, "balance inquiry for non existent account failed"

    try:
        dude.withdrawal("12345", 10000)
    except ValueError as e:
        assert str(e) == "nickel less cage", "incorrect error message for nickel less cage"

    expected_summary = "account ID: 1111, current balance: 700"
    assert dude.account_summary() == expected_summary, "account summary worked"

    print("All tests passed!")


if __name__ == '__main__':
    test()
