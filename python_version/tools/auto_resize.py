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
    # text_surface界面
    user_inputs_coonfig = app["text_surface"]["user_inputs"]
    surfaces[0].user_inputs['width'] = int(user_inputs_coonfig[0] + user_inputs_coonfig[0]*k)
    surfaces[0].user_inputs['height'] = int(user_inputs_coonfig[1] + user_inputs_coonfig[1]*k)
    save_button_config = app["text_surface"]["save_button"]
    surfaces[0].save_button['font'] = (
        '方正舒体', int(save_button_config + save_button_config*k), 'normal')
    complete_button_config = app["text_surface"]["complete_button"]
    surfaces[0].complete_button['font'] = (
        '方正舒体', int(complete_button_config + complete_button_config * k), 'normal')
    show_button_config = app["text_surface"]["show_button"]
    surfaces[0].show_button['font'] = (
        '方正舒体', int(show_button_config + show_button_config * k), 'normal')
    exit_button_config = app["text_surface"]["exit_button"]
    surfaces[0].exit_button['font'] = (
        '方正舒体', int(show_button_config + show_button_config * k), 'normal')
