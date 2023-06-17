def blite_task_level_img(level, widget, *args):
    if level == "normal":
        widget.create_oval(10, 10, int(widget['width'])-10,
                           int(widget['height'])-10, fill='white')
    elif level == 'good':
        pass
    elif level == 'great':
        pass
    elif level == 'excellent':
        pass