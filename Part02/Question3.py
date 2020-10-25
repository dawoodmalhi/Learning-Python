import itertools

lettersDic = {
    '1': ['a', 'b'], 
    '2': ['c', 'd']
}

for product in itertools.product(*[lettersDic[k] for k in sorted(lettersDic.keys())]):
    print("".join(product))
