import itertools

print(*(map(lambda x: ''.join(x), (itertools.permutations(map(
    lambda x: str(x), (range(1, int(input()) + 1))))))), sep='\n')
