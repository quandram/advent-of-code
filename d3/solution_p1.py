use_test_data = False
data_file = "test-data.txt" if use_test_data else "puzzle-data.txt"


def find_max_two_digit_combo(bank):
    d1 = max(bank[:-1])
    d2 = max(bank[(bank.index(d1) + 1):])
    print(f"{bank} = {d1 + d2}")
    return int(d1 + d2)


banks = []
with open(data_file, "r") as f:
    for line in f:
        banks.append(list(line.strip()))

print(sum(map(find_max_two_digit_combo, banks)))
