

def part_one():
    races = [(40, 215), (70, 1051), (98, 2147), (79, 1005)]
    result = 1
    for race in races:
        result *= count_ways_to_win(race)
    return result


def part_two():
    race = (40709879, 215105121471005)
    return count_ways_to_win(race)


def count_ways_to_win(race):
    time, distance_record = race
    for time_to_hold in range(0, time):
        time_to_drive = time - time_to_hold
        speed = time_to_hold
        distance_driven = speed * time_to_drive
        if distance_driven > distance_record:
            return time_to_drive - speed + 1


if __name__ == "__main__":
    print(part_one())
    print(part_two())
