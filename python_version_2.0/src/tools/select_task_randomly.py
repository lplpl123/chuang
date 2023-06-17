import numpy as np
from random import choice
from data.task_database import TASKS


def select_surface_randomly(surfaces):
    p = np.random.random()
    if p <= 0.25:
        surface = surfaces[0]
    elif p <= 0.5:
        surface = surfaces[1]
    elif p <= 0.75:
        surface = surfaces[2]
    elif p <= 1:
        surface = surfaces[3]
    return surface

def select_task_randomly(surface):
    p = np.random.random()
    if p <= 0.05:
        task = choice(TASKS.get(surface).get("excellent"))
        level = "excellent"
    elif p <= 0.20:
        task = choice(TASKS.get(surface).get("great"))
        level = "great"
    elif p <= 0.50:
        task = choice(TASKS.get(surface).get("good"))
        level = "good"
    elif p <= 1.00:
        task = choice(TASKS.get(surface).get("normal"))
        level = "normal"
    return task, level