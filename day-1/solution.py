def process(input: list[str]) -> tuple[int, int]:
    cursor: int = 50
    exact_zeroes: int = 0
    passed_zeroes: int = 0

    for line in input:
        direction: str = line[0]
        magnitude: int = int(line[1:])
        delta: int = magnitude * (1 if direction == 'R' else -1)

        prev_cursor: int = cursor
        cursor = (cursor + delta) % 100

        passed_zeroes += magnitude // 100 # full wrap arounds

        if cursor == 0:
            exact_zeroes += 1
            passed_zeroes += 1
            continue

        if prev_cursor == 0:
            continue 

        if (direction == 'L' and prev_cursor < cursor) or (direction == 'R' and prev_cursor > cursor):
            passed_zeroes += 1

    return (exact_zeroes, passed_zeroes)

with open('input.txt', 'r') as f:
    (exact_zeroes, passed_zeroes) = process(f.readlines())
    print(f'exact_zeroes: {exact_zeroes}, passed_zeroes: {passed_zeroes}')