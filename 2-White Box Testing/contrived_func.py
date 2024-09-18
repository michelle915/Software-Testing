import math


def contrived_func(val):
    a = val - math.sqrt(abs(val * 2)) > 5
    b = val ** 2 % 2 == 0
    c = val * 5 < 100
    d = -val ** 3 > 0

    if a or b:
        if (a and b) or (b and c) and d:
            pass
        else:
            pass
    else:
        if (a or b) or (b or c):
            pass
        else:
            pass

    if a and b:
        pass
    else:
        pass
