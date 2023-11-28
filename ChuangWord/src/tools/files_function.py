import datetime


""" 文本文件保存 """
def txt_file_save(task_class, task_info, task_level, work_edit_area):
    data = work_edit_area.toPlainText()
    time = str(datetime.datetime.now())
    time = time.split(" ")[0]
    file_name = task_info + "_" + time
    with open("./users_data/{}/{}/{}.txt".format(task_class, task_level, file_name),
              mode='w', encoding='utf-8') as write_file:
        write_file.write(data)
    return True
