import math
import tkinter as tk

from src import Ship
from src.stats.ship_base import ShipBase
from src import Hull


def create_circle(canvas, x, y, r, **kwargs):
    canvas.create_oval(x - r, y - r, x + r, y + r, **kwargs)


def create_arc_segment(canvas, center_x, center_y, radius1, radius2, radius3, angle, **kwargs):
    # tkinter starts arc at 90 degrees, to get north facing, 90 - 1/2(angle)
    start_angle = 90 - (angle / 2)
    extent = angle

    canvas.create_arc(center_x - radius1, center_y - radius1, center_x + radius1, center_y + radius1,
                      start=start_angle, extent=extent, style=tk.ARC, **kwargs)
    canvas.create_arc(center_x - radius2, center_y - radius2, center_x + radius2, center_y + radius2,
                      start=start_angle, extent=extent, style=tk.ARC, **kwargs)
    canvas.create_arc(center_x - radius3, center_y - radius3, center_x + radius3, center_y + radius3,
                      start=start_angle, extent=extent, style=tk.ARC, **kwargs)

    start_angle_rad = math.radians(start_angle)
    end_angle_rad = math.radians(start_angle + extent)

    x1_inner = center_x + radius1 * math.cos(start_angle_rad)
    y1_inner = center_y - radius1 * math.sin(start_angle_rad)
    x2_inner = center_x + radius1 * math.cos(end_angle_rad)
    y2_inner = center_y - radius1 * math.sin(end_angle_rad)

    x1_middle = center_x + radius2 * math.cos(start_angle_rad)
    y1_middle = center_y - radius2 * math.sin(start_angle_rad)
    x2_middle = center_x + radius2 * math.cos(end_angle_rad)
    y2_middle = center_y - radius2 * math.sin(end_angle_rad)

    x1_outer = center_x + radius3 * math.cos(start_angle_rad)
    y1_outer = center_y - radius3 * math.sin(start_angle_rad)
    x2_outer = center_x + radius3 * math.cos(end_angle_rad)
    y2_outer = center_y - radius3 * math.sin(end_angle_rad)

    canvas.create_line(center_x, center_y, x1_inner, y1_inner, **kwargs)
    canvas.create_line(center_x, center_y, x2_inner, y2_inner, **kwargs)

    canvas.create_line(x1_inner, y1_inner, x1_middle, y1_middle, **kwargs)
    canvas.create_line(x1_middle, y1_middle, x1_outer, y1_outer, **kwargs)

    canvas.create_line(x2_inner, y2_inner, x2_middle, y2_middle, **kwargs)
    canvas.create_line(x2_middle, y2_middle, x2_outer, y2_outer, **kwargs)

    canvas.create_line(x1_outer, y1_outer, x2_outer, y2_outer, **kwargs)


class TestMain:

    def test1(self):
        print("hello")

    def create_canvas_draw_ship(self):
        a = Ship(81, 6, 2, [Hull(4, 0, 1, 2, 66, 50)], 0, 0, 0, 0, ShipBase.SMALL, 0)
        root = tk.Tk()
        c = tk.Canvas(root,
                   height=root.winfo_screenheight(), width=root.winfo_screenwidth())
        c.pack()
        center_x = root.winfo_screenwidth() // 2
        center_y = root.winfo_screenheight() // 2

        c.create_rectangle(center_x - a.get_width() // 2, center_y - a.get_length() // 2,
                           center_x + a.get_width() // 2, center_y + a.get_length() // 2)
        create_circle(c, center_x, center_y - 100, 4)

        create_arc_segment(c, center_x, center_y, 300, 600, 700, 66)

        root.mainloop()
