def calc(a, b):
    return a+b, a*b
result=calc(1,3)
print(result)
result1, result2 = calc(3,3)
print(result1)
print(result2)


def calc(a, b = 10):
    return a+b, a*b
result=calc(1,3)
print(result)
result = calc(10)
print(result)

def add(a, b = 10):
    print(a)
    print(b)
    return a+b

print(add(1, 2))
print(add(1))

def sum(*values):
    result=0

    for ss in values:
        result=result+ss
    return result
result=sum(1,2,3,4,5,6)
print(result)