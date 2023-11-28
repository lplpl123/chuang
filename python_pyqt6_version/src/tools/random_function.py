import random


def generate_tem_task_data(task_from_class):
    selected_task_IDs = []
    # normal
    level_normal_tasks = task_from_class[task_from_class['level'] == 'normal']
    level_normal_tasks_ID = list(level_normal_tasks['ID'])
    for _ in range(7):
        selected_task_ID = random.choice(level_normal_tasks_ID)
        selected_task_IDs.append(selected_task_ID)
    # good
    level_good_tasks = task_from_class[task_from_class['level'] == 'good']
    level_good_tasks_ID = list(level_good_tasks['ID'])
    for _ in range(5):
        selected_task_ID = random.choice(level_good_tasks_ID)
        selected_task_IDs.append(selected_task_ID)
    # great
    level_great_tasks = task_from_class[task_from_class['level'] == 'great']
    level_great_tasks_ID = list(level_great_tasks['ID'])
    for _ in range(3):
        selected_task_ID = random.choice(level_great_tasks_ID)
        selected_task_IDs.append(selected_task_ID)
    # excellent
    level_excellent_tasks = task_from_class[task_from_class['level'] == 'excellent']
    level_excellent_tasks_ID = list(level_excellent_tasks['ID'])
    for _ in range(5):
        selected_task_ID = random.choice(level_excellent_tasks_ID)
        selected_task_IDs.append(selected_task_ID)

    return selected_task_IDs

def random_select_task(IDs):
    return random.choice(IDs)