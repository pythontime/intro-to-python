# Use range(start, stop, step=1) to loop through a list of numbers
for i in range(10):
    print(i)
print()

for i in range(10, 20):
    print(i)
print()

for i in range(10, 20, 2):
    print(i)
print()


primes = [1, 2, 3, 5, 7, 11, 13]
# Can loop over lists
for number in primes:
    print(f'The square of {number} is {number ** 2}')


# If you need to know the index, use enumerate()
for i, number in enumerate(primes):
    print(f'{i}: {number}')
