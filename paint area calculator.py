import math


test_h = int(input("Height of wall: "))
test_w = int(input("Width of wall: "))
coverage = 5
def paint_calc(height, width, cover):
    area = height * width
    number_of_can = math.ceil(area / cover)
    print(f"You'll need {number_of_can} cans of paint")


paint_calc(test_h, test_w, coverage)
