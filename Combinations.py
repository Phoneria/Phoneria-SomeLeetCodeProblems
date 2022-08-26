import itertools

n =7
k = 3


numbers = list(range(n))

print(list(itertools.combinations(numbers,k)))
