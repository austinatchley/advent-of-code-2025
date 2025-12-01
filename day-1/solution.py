def process_line(line: str, prev_cursor: int) -> int:
    direction: str = line[0]
    magnitude: int = int(line[1:])

    delta: int = magnitude if direction == 'R' else (-1 * magnitude)
    new_cursor: int = prev_cursor + delta
    if (new_cursor < 0):
        new_cursor += 100

    return new_cursor % 100

cursor: int = 50
zeroes: int = 0
with open('input.txt', 'r') as f:
    for line in f:
        cursor = process_line(line, cursor)
        if cursor == 0:
            zeroes += 1

print(zeroes)