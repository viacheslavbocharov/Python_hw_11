def is_even(number):
    number_is_even = True
    num_str = str(number)
    if num_str[-1] in ['1', '3', '5', '7', '9']:
        number_is_even = False
    return number_is_even


assert is_even(2494563894038**2) == True, 'Test1'
assert is_even(1056897**2) == False, 'Test2'
assert is_even(24945638940387**3) == False, 'Test3'