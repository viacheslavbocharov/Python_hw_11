def generate_cube_numbers(end):
    if end > 1:
        num = 2
        while True:
            num_power = num ** 3
            if num_power <= end:
                yield num_power
                num += 1
            else:
                break


print(list(generate_cube_numbers(10)))
print(list(generate_cube_numbers(100)))
print(list(generate_cube_numbers(1000)))
