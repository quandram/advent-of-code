use_test_data = False
data_file = "test-data.txt" if use_test_data else "puzzle-data.txt"


starting_location = 50
location = starting_location
password = 0
line_count = 0

with open(data_file, "r") as f:
    for line in f:
        line_count += 1
        movement = int(line[1:]) % 100
        if line[0:1] == "L":
            movement = 0 - movement

        print(f"Moving {movement} from {location}")
        location = location + movement
        if location < 0:
            location += 100
        elif location > 99:
            location -= 100
        print(f"New location: {location}")
        if location == 0:
            print("found a zero")
            password += 1

print(f"Password is: {password} from {line_count} lines")
