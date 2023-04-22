import math

def paint_calc(height, width, cover):
    paint = math.ceil((height*width)/cover)
    print(f"Buy {paint} buckets of paints.")

test_h = int(input("Enter the wall height: "))
test_w = int(input("Enter the wall weight: "))
coverage = 5
paint_calc(height=test_h, width=test_w, cover=coverage)
