import datetime
import cv2
import soundfile as sf
from PyQt5.Qt import *
from PIL import Image


""" 图片文件保存 """
def img_file_save(task_class, task_info, task_level):
    file_path = QFileDialog.getOpenFileName(None, "请从本地上传完成的任务......",
                                            "./", "All(*.*);;Images(*.png);;Images(*.jpg)")
    if not file_path[0]:
        return False
    img = Image.open(file_path[0])
    time = str(datetime.datetime.now())
    time = time.split(" ")[0]
    file_name = task_info + "_" + time
    img.save("./users_data/{}/{}/{}.png".format(task_class, task_level, file_name))
    img.close()
    return True

""" 文本文件保存 """
def txt_file_save(task_class, task_info, task_level):
    file_path = QFileDialog.getOpenFileName(None, "请从本地上传完成的任务......",
                                            "./", "All(*.*);;Images(*.txt)")
    if not file_path[0]:
        return False
    with open(file_path[0], mode='r', encoding='utf-8') as read_file:
        data = read_file.read()
    time = str(datetime.datetime.now())
    time = time.split(" ")[0]
    file_name = task_info + "_" + time
    with open("./users_data/{}/{}/{}.txt".format(task_class, task_level, file_name),
              mode='w', encoding='utf-8') as write_file:
        write_file.write(data)
    return True

""" 视频文件保存 """
def video_file_save(task_class, task_info, task_level):
    file_path = QFileDialog.getOpenFileName(None, "请从本地上传完成的任务......",
                                            "./", "All(*.*);;Images(*.mp4)")
    if not file_path[0]:
        return False
    cap = cv2.VideoCapture(file_path)
    fourcc = cv2.VideoWriter_fourcc()
    size = (int(cap.get(cv2.CAP_PROP_FRAME_WIDTH)), int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT)))
    time = str(datetime.datetime.now())
    time = time.split(" ")[0]
    file_name = task_info + "_" + time
    out = cv2.VideoWriter('./users_data/{}/{}/{}'.format(task_class, task_level, file_name),
                          fourcc, 10.0, size)
    while True:
        ret, frame = cap.read()
        # 在图像上显示 Press Q to save and quit
        out.write(frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    cap.release()
    out.release()
    return True

""" 音频文件保存 """
def audio_file_save(task_class, task_info, task_level):
    file_path = QFileDialog.getOpenFileName(None, "请从本地上传完成的任务......",
                                            "./", "All(*.*);;Images(*.mp3)")
    if not file_path[0]:
        return False
    audio, sample_rate = sf.read(file_path)
    time = str(datetime.datetime.now())
    time = time.split(" ")[0]
    file_name = task_info + "_" + time
    sf.write('./users_data/{}/{}/{}'.format(task_class, task_level, file_name), sample_rate)
    return True