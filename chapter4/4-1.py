def add_many(*args):
    print(args)
    result = 0
    for i in args:
        result += i
    return result
print(add_many(1,2,4,5,6,10))