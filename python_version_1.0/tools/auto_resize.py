from config import app


def auto_resize(event, root, lb, btn, surfaces):
    # 计算auto_resize_k
    root_width = root.winfo_width()
    root_height = root.winfo_height()
    k = min(root_width, root_height) / 400
    # auto_size主界面
    btn_config = app["main_surface"]["btn"]
    btn['width'] = int(btn_config[0] + btn_config[0] * k)
    btn['height'] = int(btn_config[1] + btn_config[1] * k)
    lb_config = app["main_surface"]["lb"]
    lb['font'] = ('方正舒体', int(lb_config + lb_config*k), 'normal')
    button_config = app["button_size"]
    # text_surface界面
    surfaces[0].user_inputs['width'] = int(root_width / 10)
    surfaces[0].user_inputs['height'] = int(root_height / 20)
    surfaces[0].save_button['font'] = (
        '方正舒体', int(button_config + button_config*k), 'normal')
    surfaces[0].complete_button['font'] = (
        '方正舒体', int(button_config + button_config * k), 'normal')
    surfaces[0].show_button['font'] = (
        '方正舒体', int(button_config + button_config * k), 'normal')
    surfaces[0].exit_button['font'] = (
        '方正舒体', int(button_config + button_config * k), 'normal')
    # photograph_surface界面
    surfaces[1].exit_button['font'] = (
        '方正舒体', int(button_config + button_config * k), 'normal')
    surfaces[1].upload_button['font'] = (
        '方正舒体', int(button_config + button_config * k), 'normal')
    # video_surface界面
    surfaces[2].exit_button['font'] = (
        '方正舒体', int(button_config + button_config * k), 'normal')
    surfaces[2].upload_button['font'] = (
        '方正舒体', int(button_config + button_config * k), 'normal')
    # audio_surface界面
    surfaces[3].exit_button['font'] = (
        '方正舒体', int(button_config + button_config * k), 'normal')
    surfaces[3].upload_button['font'] = (
        '方正舒体', int(button_config + button_config * k), 'normal')