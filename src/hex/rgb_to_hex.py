# def rgb(r, g, b):
#    round = lambda x: min(255, max(x, 0))
#    return ("{:02X}" * 3).format(round(r), round(g), round(b))

def rgb(r, g, b):
    """
The rgb function is incomplete. Complete it so that passing in RGB decimal values will result in a hexadecimal
representation being returned. Valid decimal values for RGB are 0 - 255. Any values that fall out of that
range must be rounded to the closest valid value.

    :rtype: str Hex value
    """
    return to_hex(r) + to_hex(g) + to_hex(b)


def to_hex(num):
    if num >= 255: return 'FF'
    if num < 1: return '00'
    return hex(num)[2::].zfill(2).upper()


if __name__ == '__main__':
    print(rgb(1, 2, 3))
