

def auto_resize(event, root, lb, btn):
    # 传入一个组件
    # 然后改变它的长和宽，如果有内容的话，再变内容
    wide = 80
    height = 60
    re_size = 10
    root_width = root.winfo_width()
    root_height = root.winfo_height()
    k = min(root_width, root_height) / 400
    re_size = int(re_size + re_size*k)
    lb['font'] = ('方正舒体', re_size, 'normal')
    btn['width'] = int(wide + wide*k)
    btn['height'] = int(height + height * k)