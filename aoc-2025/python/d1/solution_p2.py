use_test_data = False
data_file = "test-data.txt" if use_test_data else "puzzle-data.txt"


starting_location = 50
location = starting_location
password = 0
line_count = 0

with open(data_file, "r") as f:
    for line in f:
        line_count += 1
        init_location = location
        init_password = password
        movement = int(line[1:])
        password += movement // 100
        movement = movement % 100

        if line[0:1] == "L":
            movement = 0 - movement

        location = location + movement

        if location == 0:
            password += 1
        elif location < 0:
            location += 100
            if init_location != 0:
                password += 1
        elif location > 99:
            location -= 100
            if init_location != 0:
                password += 1

        print(f"{line_count}: Moving {movement} from {init_location} to {
            location}. Password {init_password} -> {password}")

print(f"Password is: {password} from {line_count} lines")
