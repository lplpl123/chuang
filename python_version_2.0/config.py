TASK_NUM = 5

app = {
    "width": 800,
    "height": 600,
    "background": "white",
    "name": "窗"
}

button_label = {
    "width": 80,
    "height": 60,
    "text_size": 10
}

main_surface_data = {
    "imgs": {
        "background": {
            "tol_frames": 101,
            "original_img": "./resources/originals/jijian02.gif",
            "output_imgs": "./resources/surfaces_imgs/main_surface_imgs/background"
        },
    }
}

loading_surface = {
    "imgs": {
        "loading": {
            "tol_frames": 246,
            "original_img": "./resources/originals/loading.gif",
            "output_imgs": "./resources/surfaces_imgs/main_surface_imgs/loading"
        },
    }
}