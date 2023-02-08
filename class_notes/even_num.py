def get_even_func(numbers):
    even_numbers = [num for num in numbers if not num % 2]
    return even_numbers

print(get_even_func([1, 2, 3, 4, 5, 6]))
