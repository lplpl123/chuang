from tools import setup
from surfaces.main_surface import mainSurface


if  __name__ == '__main__':
    root = setup.setup()
    mainsurface = mainSurface(root)
    setup.run(root)