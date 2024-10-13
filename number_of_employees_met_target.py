def numberOfEmployeesWhoMetTarget(self, hours: list[int], target: int) -> int:
    result = 0
    for hour in hours:
        if hour >= target:
            result += 1
    return result


def numberOfEmployeesWhoMetTarget_2(self, hours: list[int], target: int) -> int:
    return len([hour for hour in hours if hour >= target])
