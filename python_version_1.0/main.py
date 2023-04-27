from tools import setup
from surfaces.main_surface import mainSurface


if  __name__ == '__main__':
    root = setup.setup()
    task_num = 5
    mainsurface = mainSurface(root, task_num)
    setup.run(root)