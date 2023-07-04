import math


def gcd(x, y):
    """
    輾轉相除法
    使用的公式 y 要比 x 小, 所以在第一步處理
    """
    if y < x:
        x, y = y, x

    while y > 0:
        # print(x, y)
        x, y = y, x % y
        # print("--------", x, y)

    return x


if __name__ == "__main__":
    assert math.gcd(12, 10) == gcd(12, 10)
    assert math.gcd(1934, 172) == gcd(1934, 172)
    assert math.gcd(298314291, 9383912) == gcd(298314291, 9383912)
