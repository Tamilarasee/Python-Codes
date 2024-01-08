def find_max(numbers):
    maximum=numbers[0]
    for i in numbers:
        if maximum<i:
            maximum=i
    return maximum