def baskhara(a, b, c):
    # retorne None se discriminante < 0
    # retorne apenas um valor se discriminante == 0
    # retorne [x1, x2] nos outros casos
    discriminante = b ** 2 - 4 * a * c
    
    if discriminante < 0:
        return None
    if discriminante == 0:
        return discriminante
    elif discriminante > 0:
        x1 = (-b + (discriminante ** (1/2))) / (2 * a)
        x2 = (-b - (discriminante ** (1/2))) / (2 * a)
        return [x2, x1]

def test():
    #assert baskhara(1, -3, 2) == [2, 1]
    assert baskhara(2, 3, -2) == [-2, 0.5]
    assert baskhara(1, -5, 6) == [2, 3]
    assert baskhara(1, -7, 10) == [2, 5]

    assert baskhara(1, 2, 3) is None
    assert baskhara(1, 0, 0) == 0

print(baskhara(1, 0, 0) == 0)