def get_employee_timeframe(logs, employee_id):

    first_index = -1
    second_index = -1

    for index, value in enumerate(logs):
        if value == employee_id:
            if first_index == -1:
                first_index = index
            elif second_index == -1:
                second_index = index
                break

    if first_index == -1:
        return ()
    if second_index == -1:
        return logs[first_index:]
    return logs[first_index:second_index + 1]


print(get_employee_timeframe((1, 2, 3), 8))
print(get_employee_timeframe((1, 8, 3, 4, 8, 8, 9, 2), 8))
print(get_employee_timeframe((1, 2, 8, 5, 1, 2, 9), 8))