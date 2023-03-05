# function receives list of iterables and returns list of interluding elements

def interleave(*args):
    result = []
    for i in range(len(args[0])):
        for arg in args:
            result.append(arg[i])
    return result

print(interleave('abc', [1, 2, 3], ('!', '@', '#')))