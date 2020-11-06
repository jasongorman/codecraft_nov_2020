def sqrt(number):
    root = number / 2
    last = 0

    while abs(root - last) > 0:
        last = root
        root = (root + (number / root)) / 2

    return root