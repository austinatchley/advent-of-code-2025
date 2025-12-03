def invalid(num: int) -> bool:
    string_representation: str = str(num)
    for index in range(1, len(string_representation)):
        substring = string_representation[:index]
        if (substring + substring) == string_representation:
            # print(f'{num} invalid!')
            return True
    return False

password: int = 0
with open('input.txt', 'r') as f:
    for num_range in f.read().split(','):
        tokens = num_range.split('-')
        start = int(tokens[0])
        end = int(tokens[1])

        for n in [i for i in range(start, end) if invalid(i)]:
            password += n

print(password)