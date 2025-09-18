def euclid(a, b):
    if a == 0:
        return (b, 0, 1)
    gcd, x1, y1 = euclid(b % a, a)
    koeff_x = y1 - (b//a) * x1
    koeff_y = x1
    return (gcd, koeff_x, koeff_y)

print(euclid(240,46))