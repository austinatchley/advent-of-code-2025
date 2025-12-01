def process_line(line: str, prev_cursor: int) -> tuple[int, int]:
    direction: str = line[0]
    magnitude: int = int(line[1:])

    passed_zero: int = 0 # int(magnitude / 100)

    delta: int = magnitude if direction == 'R' else (-1 * magnitude)
    new_cursor: int = prev_cursor + delta

    if (new_cursor == 0 and prev_cursor != 0):
        passed_zero += 1
    if prev_cursor == 0 and new_cursor < 0:
        passed_zero -= 1

    while (new_cursor < 0):
        new_cursor += 100
        passed_zero += 1
    while (new_cursor >= 100):
        new_cursor -= 100
        passed_zero += 1
    
    print(f'{prev_cursor} + {direction}{magnitude} -> {new_cursor}')
    if passed_zero != 0:
        print(f'passed zero: {passed_zero}')


    return (new_cursor, passed_zero)

cursor: int = 50
zeroes: int = 0
with open('input.txt', 'r') as f:
    for line in f:
        (cursor, passed_zero) = process_line(line, cursor)
        zeroes += passed_zero

print(zeroes)