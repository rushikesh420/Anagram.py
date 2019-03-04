def find_largest(numbers):
    if len(numbers) == 1:
            return numbers[0]
    else:
        m = find_largest(numbers[1:])
    return m if m > numbers[0] else numbers[0]
