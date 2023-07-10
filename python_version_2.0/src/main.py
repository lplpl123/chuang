import time
import multiprocessing
from tools import setup
from tools.waiting_init import WaitingInit


def loading():
    # 加载中
    waiting_init = WaitingInit()
    waiting_init.run()


if __name__ == '__main__':
    loading_process = multiprocessing.Process(target=loading)
    loading_process.start()
    run = setup.Run()
    loading_process.terminate()
    time.sleep(1)
    run.run()