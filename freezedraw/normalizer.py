def normalize(input, min, max):
    return (max-min)*input+min


def clamp(input, min, max):
    if input < min:
        input = min
    if input > max:
        input = max
