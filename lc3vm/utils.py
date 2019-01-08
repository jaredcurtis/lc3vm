def set_bits(int_, offsets):
    for offset in offsets:
        mask = 1 << offset
        int_ = int_ | mask
    return int_
