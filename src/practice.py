def args(str, result=None):
    '''
    test
    aaaaa
    '''
    print(result)
    if result == None:
        result = []
    result.append(str)
    return result

test = ['a','b']

print(args('c'))
print(args('c', test))
print(args.__doc__)
    