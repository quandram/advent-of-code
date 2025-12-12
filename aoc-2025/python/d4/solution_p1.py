use_test_data = False
data_file = "test-data.txt" if use_test_data else "puzzle-data.txt"


def get_count_of_items_within_x_adjacent(floor_plan, marker_empty, marker_full, adjacency, max_value):
    max_x = len(floor_plan[0])
    max_y = len(floor_plan)
    adjacency_matrix = [[0 for _ in range(max_x)] for _ in range(max_y)]
    for y in range(0, max_y):
        for x in range(0, max_x):
            if floor_plan[y][x] == marker_empty:
                adjacency_matrix[y][x] = max_value
            if floor_plan[y][x] == marker_empty:
                continue
            for offset_y in range(-adjacency, adjacency + 1):
                for offset_x in range(-adjacency, adjacency + 1):
                    if offset_x == 0 and offset_y == 0:
                        continue

                    update_x = x + offset_x
                    if update_x >= max_x or update_x < 0:
                        continue

                    update_y = y + offset_y
                    if update_y >= max_y or update_y < 0:
                        continue

                    adjacency_matrix[update_y][update_x] += 1
    return adjacency_matrix


floor_plan = []
with open(data_file, "r") as f:
    for line in f:
        floor_plan.append(list(line.strip()))


adjacency_matrix = get_count_of_items_within_x_adjacent(
    floor_plan, ".", "@", 1, 99)

result = [x for row in adjacency_matrix for x in row if x < 4]

print(result)
print(len(result))
