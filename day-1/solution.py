def process(input: list[str]) -> tuple[int, int]:
    cursor: int = 50
    exact_zeroes: int = 0
    passed_zeroes: int = 0

    for line in input:
        direction: str = line[0]
        magnitude: int = int(line[1:])

        if direction == 'L':
            if cursor - magnitude <= 0:
                passed_zeroes += (100 - cursor + magnitude) // 100
            if cursor == 0:
                passed_zeroes -= 1
            cursor = (cursor - magnitude) % 100
        else:
            passed_zeroes += (cursor + magnitude) // 100
            cursor = (cursor + magnitude) % 100
        
        if cursor == 0:
            exact_zeroes += 1

    return (exact_zeroes, passed_zeroes)

with open('input.txt', 'r') as f:
    (exact_zeroes, passed_zeroes) = process(f.readlines())
    print(f'exact_zeroes: {exact_zeroes}, passed_zeroes: {passed_zeroes}')