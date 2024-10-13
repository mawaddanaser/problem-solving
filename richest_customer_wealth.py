def maximumWealth(self, accounts: list[list[int]]) -> int:
    highest_sum = 0
    for account in accounts:
        current_sum = sum(account)
        if highest_sum < current_sum:
            highest_sum = current_sum

    return highest_sum


def maximumWealth_2(self, accounts: list[list[int]]) -> int:
    return max([sum(account) for account in accounts])
