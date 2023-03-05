def join(*args, sep = '-'):
    result = []
    if len(args) == 0:
        return None
    for arg in args:
        for element in arg:
            result.append(element)
        result.append(sep)
    result.pop()
    return result

print(join([1, 2], [8], [9, 5, 6], sep='@'))
print(join([1]))
print(join())