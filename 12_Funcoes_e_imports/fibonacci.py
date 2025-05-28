def fibonacci(x):
    if x < 0:
        return None
    elif x == 0:
        return 0
    elif x == 1:
        return 1
    else:
        return fibonacci(x - 1) + fibonacci(x - 2)
    

def test():
    assert fibonacci(-1) is None
    assert fibonacci(0) == 0
    assert fibonacci(1) == 1
    assert fibonacci(2) == 1
    assert fibonacci(3) == 2
    assert fibonacci(4) == 3
    assert fibonacci(5) == 5
    assert fibonacci(10) == 55

print(fibonacci(-1) is None)
print(fibonacci(0) == 0)
print(fibonacci(1) == 1)
print(fibonacci(2) == 1)
print(fibonacci(3) == 2)
print(fibonacci(4) == 3)
print(fibonacci(5) == 5)
print(fibonacci(10) == 55)