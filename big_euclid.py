def euclid(koeff_x,koeff_y):
    if koeff_x == 0:
        return (koeff_y, 0, 1)
    gcd, x1, y1 = euclid(koeff_y % koeff_y, koeff_x)
    x = y1 - (koeff_y//koeff_x) * x1
    y = x1
    return (gcd, x, y)

print(euclid(240,46))