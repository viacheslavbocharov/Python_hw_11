def prime_generator(end):
    if end > 1:
        for num in range(2, end + 1):
            is_num_prime = True

            for i in range(2, num):
                if num % i == 0:
                    is_num_prime = False
                    break

            if is_num_prime:
                yield num


from inspect import isgenerator

gen = prime_generator(1)
assert isgenerator(gen) == True, 'Test0'
assert list(prime_generator(10)) == [2, 3, 5, 7], 'Test1'
assert list(prime_generator(15)) == [2, 3, 5, 7, 11, 13], 'Test2'
assert list(prime_generator(29)) == [2, 3, 5, 7, 11, 13, 17, 19, 23, 29], 'Test3'
print(list(prime_generator(0)))
print(list(prime_generator(1)))
print(list(prime_generator(10)))
print(list(prime_generator(15)))
print(list(prime_generator(29)))
print('Ok')
