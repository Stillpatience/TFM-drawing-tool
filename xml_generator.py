import math
import os

from PIL import Image

from color import Color
from drawing import Drawing
from line import Line
from point import Point


def calculate_thickness(distance):
    return int(math.sqrt(2 * (distance ** 2)))


def get_maximum_size():
    return 20000


def rgb_to_hex(rgb):
    return '%02x%02x%02x' % rgb[:3]


def generate_xml(d=1, img_directory="static/images/uploads", img_name="test.jpg", out_file="result.xml",  out_dir="outputs", x_offset=0, y_offset=0):
    im = Image.open(os.path.join(img_directory, img_name))
    pix = im.load()
    first_y, last_y, curr_x, lines, prev_color = 0, 0, 0, [], pix[0, 0]
    thickness = calculate_thickness(d)
    for x in range(0, im.size[0], d):
        for y in range(0, im.size[1], d):
            color = pix[x, y]
            if curr_x == x and color == prev_color:
                last_y = y
            else:
                if first_y == last_y:
                    lines.append(
                        Line(
                            Point(x_offset + x, y_offset + first_y),
                            Point(x_offset + x, y_offset + last_y + 1),
                            Color(prev_color),
                            thickness,
                        )
                    )
                else:
                    lines.append(
                        Line(
                            Point(x_offset + x, y_offset + first_y),
                            Point(x_offset + x, y_offset + last_y),
                            Color(prev_color),
                            thickness,
                        )
                    )
                prev_color = color
                first_y = y
                last_y = y
                curr_x = x
    drawing = Drawing(lines)

    if len(str(drawing)) < get_maximum_size():
        print("Reached an accuracy of: " + str(d))
        output_file = open(os.path.join(out_dir, out_file), "w")
        output_file.write(str(drawing))
        return str(drawing)
    else:
        return generate_xml(d=d + 1, img_directory=img_directory, img_name=img_name, out_dir=out_dir, out_file=out_file, x_offset=x_offset, y_offset=y_offset)

