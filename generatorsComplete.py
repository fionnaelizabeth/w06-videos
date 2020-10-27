# generators


def natural_seq():
    num = 1
    while True:
        yield num
        num += 1


gen_nat = natural_seq()
print(next(gen_nat))

print('I am chilling')
a = 1000

print(next(gen_nat))
