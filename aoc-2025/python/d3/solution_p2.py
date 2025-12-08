use_test_data = False
data_file = "test-data.txt" if use_test_data else "puzzle-data.txt"


def find_max_x_digit_number(bank, x):
    result = ""
    last_char = 0
    search_from_index = 0
    print(bank)
    for i in range(1, x + 1):
        searchable_bank = get_viable_subset_from_bank(
            bank, search_from_index, x - i)
        last_char = max(searchable_bank)
        search_from_index = bank.index(
            last_char, search_from_index) + 1
        result += last_char
    return int(result)


def get_viable_subset_from_bank(bank, start_char, min_remaining_chars):
    return bank[start_char:(len(bank)-min_remaining_chars)]


banks = []
with open(data_file, "r") as f:
    for line in f:
        banks.append(list(line.strip()))

print(sum(map(lambda x: find_max_x_digit_number(x, 12), banks)))
