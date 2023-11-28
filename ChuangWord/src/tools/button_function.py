import os
import sys
import datetime
import random
import cv2
from tools import surfaces_function
from tools import files_function
from tools import task_check


def main_start_button(app, main_window, main_frame, databasefunction):
    # 1. 隐藏当前界面
    main_frame.hide()
    # 2. 从数据库读取任务
    # 更新日期
    last_day = databasefunction.get_last_date_item()
    if not last_day:
        databasefunction.create_date()
        last_day = databasefunction.get_last_date_item()
    time_read = last_day["date"]
    time_now = str(datetime.datetime.now())
    time_now = time_now.split(" ")[0]
    time_now_list = time_now.split("-")
    time_now = "/".join(time_now_list)
    if time_read != time_now:
        databasefunction.create_date()
        last_day = databasefunction.get_last_date_item()
    # 判断日期任务状态
    if last_day["done_or_not"] == "done":
        surfaces_function.create_finish_surface(app, main_window, main_frame)
    task_ID = databasefunction.read_current_task()
    # 3. 生成任务界面
    task_item = databasefunction.get_task_item(task_ID)
    surfaces_function.create_surface(app, main_window, main_frame, task_item)

def exit_button(app):
    sys.exit(app.exec_())

def work_done_button(app, main_window, main_frame, sub_frame,
                     task_class, task_info,
                     task_level, task_related_words,
                     databasefunction, work_edit_area,
                     title_task_text, work_start_button,
                     work_sure_button, done_task_num):
    # 0. 判断任务是否合规
    if_done = task_check.check_if_done(task_info, task_related_words, work_edit_area)
    if if_done != "成功":
        work_start_button.hide()
        title_task_text.setText(if_done)
        work_sure_button.show()
        return None
    # 1. 保存文件
    if task_class == "text":
        res = files_function.txt_file_save(task_class, task_info, task_level, work_edit_area)
    if res:
        # 2. 数据库修改
        databasefunction.update_task_status()
        # 3. 检查是否满足5个任务
        current_done_task_num = databasefunction.get_current_task_num()
          # 如果满足，清空数据库，创建结束页面，标记今日任务已完成
        if current_done_task_num >= done_task_num:
            databasefunction.clear_current_tasks()
            databasefunction.update_date_status()
            surfaces_function.create_finish_surface(app, main_window, main_frame)
        # 3. 关闭当前窗口
        sub_frame.deleteLater()
        surfaces_function.create_reward_surface(app, main_window, main_frame, task_class, task_level)

def text_work_show_button(app, main_window, main_frame, task_class,
                          task_level, title_task_text, work_contents_label,
                          work_date_label):
    # 读取相关文件夹下的所有文件，生成列表
    file_list = os.listdir("./users_data/{}/{}".format(task_class, task_level))
    print(file_list)
    # 从列表中挑选一个文件
    selected_file_name = random.choice(file_list)
    task_contents = selected_file_name.split('_')[0]
    task_date = selected_file_name.split('_')[1]
    # 打开文件，读取文本内容
    file_path = "./users_data/{}/{}/{}".format(task_class, task_level, selected_file_name)
    with open(file_path, encoding='utf-8', mode='r') as file:
        data = file.read()
    date = "您在" + task_date + "完成了自己的想法！"
    # 内容显示
    title_task_text.setText(task_contents)
    work_date_label.setText(date)
    work_contents_label.setText(data)

def work_sure_button(work_sure_button, title_task_text,
                     task_info, work_start_button):
    work_sure_button.hide()
    title_task_text.setText(task_info)
    work_start_button.show()

def complete_button(main_frame, reward_main_frame):
    reward_main_frame.deleteLater()
    main_frame.show()
