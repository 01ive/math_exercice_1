import itertools

possible_numbers = list(range(10))

def check(sequence):
    for i in range(1, 11):
        number = int(''.join([str(text) for text in sequence[0:i]]))
        if(number%i != 0):
            return False
    return True

for subset in itertools.permutations(possible_numbers):
    if check(subset):
        print(str(subset) + " Working !!!!!!!!!!")
        