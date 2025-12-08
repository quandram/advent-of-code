use_test_data = False
data_file = "test-data.txt" if use_test_data else "puzzle-data.txt"


def get_invalid_ids(r):
    result = []
    for id in range(r[0], r[1] + 1):
        if is_invalid_id(id):
            result.append(id)
    return result


def is_invalid_id(id):
    str_id = str(id)
    if len(str_id) % 2 == 1:
        return False
    if str_id[0:(len(str_id)//2)] == str_id[len(str_id)//2:]:
        return True
    return False


ranges = []

with open(data_file, "r") as f:
    for line in f:
        ranges = [tuple(map(int, pair.split("-")))
                  for pair in line.split(",")]

invalid_ids = list(map(get_invalid_ids, ranges))

print(sum([item for sublist in invalid_ids for item in sublist]))
