from config import app, button_label, main_surface_data

imgs = main_surface_data.get("imgs")
for key, value in imgs.items():
    print(key)
    print(value)