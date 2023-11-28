import random
import datetime
import pandas as pd
from tools.random_function import random_select_task, generate_tem_task_data


class databaseFunction():

    def __init__(self):
        self.current_tasks_data = pd.read_excel("./databases/current_tasks.xlsx", sheet_name="Sheet1")
        self.tol_tasks_data = pd.read_excel("./databases/tol_tasks.xlsx", sheet_name="Sheet1")
        self.everyday_tasks_data = pd.read_excel("./databases/everyday_tasks.xlsx", sheet_name="Sheet1")

    def read_current_task(self):
        # 1. 读取excel文件
        data = self.current_tasks_data
        # 2. 操作数据，找到还未完成的任务
        task_num = len(data)
        if task_num == 0:
            return self.create_task()
        done_or_not = data.loc[task_num-1, 'done_or_not']
        if done_or_not == "not":
            return data.loc[task_num-1, 'outer_ID']
        # 3. 生成新的任务
        return self.create_task()

    def get_task_item(self, task_ID):
        data = self.tol_tasks_data
        # 获取task的surface
        task_item = data.loc[task_ID-1]
        task_item = dict(task_item)
        return task_item

    def get_current_task_num(self):
        data = self.current_tasks_data
        return len(data)

    def update_task_status(self):
        data = self.current_tasks_data
        task_num = len(data)
        data.loc[task_num - 1, 'done_or_not'] = "done"
        data.to_excel('./databases/current_tasks.xlsx', index=False)

    def create_task(self):
        # 1. 随机挑选任务的大类
        task_list = ["text", "photo", "video", "audio"]
        random_task_class = random.choice(task_list)
        # 2. 随机挑选这个类别的一个任务
        data = self.tol_tasks_data
        task_from_class = data[data['surface'] == random_task_class]
        selected_task_IDs = generate_tem_task_data(task_from_class)
        random_task_ID = random_select_task(selected_task_IDs)
        # 3. 把挑选出来的任务写入到数据库中
        current_data = self.current_tasks_data
        row = data[data["ID"] == random_task_ID]
        row_update = {
            'content': row['content'],
            'level': row['level'],
            'surface': row['surface'],
            'done_or_not': "not",
            'outer_ID': row['ID']
        }
        row_update = pd.DataFrame(row_update)
        update_current_data = current_data.append(row_update)
        update_current_data.to_excel('./databases/current_tasks.xlsx', index=False)
        return random_task_ID

    def clear_current_tasks(self):
        data = self.current_tasks_data
        for i in range(len(data)):
            data = data.drop([0])

    def get_last_date_item(self):
        data = self.everyday_tasks_data
        length = len(data)
        if length == 0:
            return None
        date_last_item = dict(data.loc[length - 1])
        return date_last_item

    def update_date_status(self):
        data = self.everyday_tasks_data
        length = len(data)
        data.loc[length - 1, 'done_or_not'] = "done"
        data.to_excel('./databases/everyday_tasks.xlsx', index=False)

    def create_date(self):
        date_data = self.everyday_tasks_data
        time_now = str(datetime.datetime.now())
        time_now = time_now.split(" ")[0]
        time_now_list = time_now.split("-")
        time_now = "/".join(time_now_list)
        row_update = {
            'date': time_now,
            'done_or_not': "not",
        }
        row_update = pd.DataFrame(row_update, index=[0])
        update_current_data = date_data.append(row_update)
        update_current_data.to_excel('./databases/everyday_tasks.xlsx', index=False)