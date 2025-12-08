use_test_data = False
data_file = "test-data.txt" if use_test_data else "puzzle-data.txt"


def get_invalid_ids(r):
    result = 0
    for id in range(r[0], r[1] + 1):
        if is_invalid_id(id):
            result += id
    return result


def is_invalid_id(id):
    str_id = str(id)
    for c in range(1, (len(str_id) // 2) + 1):
        if len(str_id) % c != 0:
            continue
        groups = [str_id[i:i+c] for i in range(0, len(str_id), c)]
        if (all(x == groups[0] for x in groups)):
            return True
    return False


ranges = []

with open(data_file, "r") as f:
    for line in f:
        ranges = [tuple(map(int, pair.split("-")))
                  for pair in line.split(",")]

print(sum(map(get_invalid_ids, ranges)))
