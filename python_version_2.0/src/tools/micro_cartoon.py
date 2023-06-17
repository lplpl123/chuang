def mouse_slip_on_widget(event, widget, color):
    widget['fg'] = color

def mouse_slip_off_widget(event, widget, color):
    widget['fg'] = color

def expand(event, widget):
    text_size = widget['font'].split(" ")[1]
    for i in range(10):
        text_size = int(text_size) + 1
        widget['font'] = ('微软雅黑', text_size, 'normal')

def reduce(event, widget):
    text_size = widget['font'].split(" ")[1]
    for i in range(10):
        text_size = int(text_size) - 1
        widget['font'] = ('微软雅黑', text_size, 'normal')