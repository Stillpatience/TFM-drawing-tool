import math
import os
from PIL import Image

from Color import Color
from Drawing import Drawing
from Line import Line
from Point import Point


def convert_lines_to_xml(lines):
    result = []
    for line in lines:
        result.append(str(line))
    return result


def calculate_thickness(distance):
    return int(math.sqrt(2 * (distance ** 2)))


def generate_xml(d=1, file_name="test.jpg", out_file="result.xml"):
    im = Image.open(file_name)
    pix = im.load()
    first_y = 0
    prev_color = pix[0, 0]
    last_y = 0
    curr_x = 0
    lines = []
    thickness = calculate_thickness(d)
    for x in range(0, im.size[0], d):
        for y in range(0, im.size[1], d):
            color = pix[x, y]
            if curr_x == x and color == prev_color:
                last_y = y
            else:
                if first_y == last_y:
                    lines.append(Line(Point(x, first_y), Point(x, last_y+1), Color(prev_color), thickness))
                else:
                    lines.append(Line(Point(x, first_y), Point(x, last_y), Color(prev_color), thickness))
                prev_color = color
                first_y = y
                last_y = y
                curr_x = x
    drawing = Drawing(lines)

    if len(str(drawing)) < 60000:
        print("Reached an accuracy of: " + str(d))
        output_file = open(out_file, "w")
        output_file.write(str(drawing))
        return
    else:
        generate_xml(d=d + 1, file_name=file_name, out_file=out_file)



generate_xml(file_name="felix.jpg")
