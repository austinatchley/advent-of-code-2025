def invalid(i: int) -> bool:
    return True

def process_range(start: int, end: int) -> list[int]:
    invalid_nums: list[int] = list()
    for i in range(start, end):
        if invalid(i):
            invalid_nums.append(i)
    return invalid_nums

password: int = 0
with open('input.txt', 'r') as f:
    for num_range in f.read().split(','):
        tokens = num_range.split('-')
        start = int(tokens[0])
        end = int(tokens[1])

        invalid_nums = process_range(start, end)
        for n in invalid_nums:
            password += n

print(password)