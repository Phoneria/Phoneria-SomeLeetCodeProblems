import itertools




numbers = [1,2,3]
subsets = []
for k in range(len(numbers)):
    subsets.append(list(itertools.combinations(numbers,k)))
print(subsets)