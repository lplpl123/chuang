import math as m


def blite_task_level_img(level, widget, *args):
    # circle
    if level == "normal":
        widget.create_oval(10, 10, int(widget['width'])-10,
                           int(widget['height'])-10, fill='white')
    elif level == 'good':
        widget.create_polygon(int(widget['width'])/2, 10,
                              10, int(widget['height'])-10,
                              int(widget['width'])-10, int(widget['height'])-10,
                              fill='white')
    elif level == 'great':
        widget.create_polygon(10, 10,
                              int(widget['width'])-10, 10,
                              int(widget['width'])-10, int(widget['height'])-10,
                              10, int(widget['height'])-10,
                              fill="white")
    elif level == 'excellent':
        center_x = int(widget['width'])/2
        center_y = int(widget['width'])/2
        r = center_x - 6
        points = [
            # A顶点
            center_x - int(r * m.sin(2 * m.pi / 5)),
            center_y - int(r * m.cos(2 * m.pi / 5)),
            # C顶点
            center_x + int(r * m.sin(2 * m.pi / 5)),
            center_y - int(r * m.cos(2 * m.pi / 5)),
            # E顶点
            center_x - int(r * m.sin(m.pi / 5)),
            center_y + int(r * m.cos(m.pi / 5)),
            # B顶点
            center_x,
            center_y - r,
            # D顶点
            center_x + int(r * m.sin(m.pi / 5)),
            center_y + int(r * m.cos(m.pi / 5)),
        ]

        widget.create_polygon(points,
                              outline='',
                              fill='white')