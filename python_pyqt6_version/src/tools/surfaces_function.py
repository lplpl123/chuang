from surfaces.text_surface import TextSurface
from surfaces.photo_surface import PhotoSurface
from surfaces.video_surface import VideoSurface
from surfaces.audio_surface import AudioSurface
from surfaces.finish_surface import FinishSurface
from surfaces.reward_surface import RewardSurface


def create_surface(app, main_window, main_frame, task_item):
    task_class = task_item["surface"]
    if task_class == "text":
        surface = TextSurface(app, main_window, main_frame, task_item)
    elif task_class == "photo":
        surface = PhotoSurface(app, main_window, main_frame, task_item)
    elif task_class == "video":
        surface = VideoSurface(app, main_window, main_frame, task_item)
    elif task_class == "audio":
        surface = AudioSurface(app, main_window, main_frame, task_item)
    # AudioSurface(app, main_window, main_frame, surface_class, task_info)

def create_finish_surface(app, main_window, main_frame):
    FinishSurface(app, main_window, main_frame)

def create_reward_surface(app, main_window, main_frame, task_class, task_level):
    RewardSurface(app, main_window, main_frame, task_class, task_level)
