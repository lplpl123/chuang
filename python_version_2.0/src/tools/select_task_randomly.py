import numpy as np
import config


def select_task_randomly():
    surfaces = list(config.surfaces.keys())
    p = np.random.random()
    if p <= 0.25:
        task = surfaces[0]
    elif p <= 0.5:
        task = surfaces[1]
    elif p <= 0.75:
        task = surfaces[2]
    elif p <= 1:
        task = surfaces[3]
    return task