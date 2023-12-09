def part_one(games, max):
    counter = 0
    r_max, g_max, b_max = max
    for idx, game in enumerate(games):
        r_game, g_game, b_game = game
        if r_game <= r_max and g_game <= g_max and b_game <= b_max:
            counter += idx + 1
    return counter


def part_two(games):
    total = 0
    for game in games:
        r_game, g_game, b_game = game
        total += r_game * g_game * b_game
    return total


def parse_line(line):
    rgb = (0, 0, 0)
    game = line.split(':')[1]
    sets = game.split(';')
    for set in sets:
        takes = set.split(',')
        for take in takes:
            r, g, b = rgb
            count_and_color = take.strip().split(' ')
            count = int(count_and_color[0])
            color = count_and_color[1]
            match color:
                case 'red':
                    r = max(r, count)
                case 'green':
                    g = max(g, count)
                case 'blue':
                    b = max(b, count)
            rgb = (r, g, b)
    return rgb


with open('res/day02.txt') as f:
    inputs = [
        parse_line(line)
        for line in f.read().splitlines()
    ]
    print(part_one(inputs, (12, 13, 14)))
    print(part_two(inputs))
