def equal_devider(height, width):
    decision_maker = max(height, width) % min(height, width)
    if decision_maker == 0:
        return min(height, width)

    return equal_devider(min(height, width), decision_maker)


print(equal_devider(40, 15))
