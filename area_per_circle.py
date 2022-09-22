#!/usr/bin/env python
# Copyright(c) 2022 Ioana Marinescu All rights reserved.
# Created By: Ioana Marinescu

# Date: Sept. 21, 2022
# calculates the area and perimeter of a circle with a radius of 3


import math


def main():
    # constants
    RADIUS = 3

    # area and circumference calculations
    area = math.pi * math.pow(RADIUS, 2)
    circumference = 2 * math.pi * RADIUS

    # printing the results
    print("For a circle with a radius of 3cm")
    print("The area is: {}cm^2".format(area))
    print("The circumference is: {}cm".format(circumference))


if __name__ == "__main__":
    main()
