with open("C:/Users/75882/Desktop/my world/projects/chuang/python_version_2.0/src/data/current_tasks", mode='r', encoding='utf-8') as file:
    current_task_info = file.read()
    current_task_info = current_task_info.split('\n')
    print(current_task_info)