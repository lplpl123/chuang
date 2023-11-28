from tools.check_task_function import checkFunction


def check_if_done(task_info, task_related_words, work_edit_area):
    check_function = checkFunction(work_edit_area, task_related_words)
    res = common_style_check(check_function)
    if res != "成功":
        return res
    if task_info == "请根据你现在的心境，创作一首诗......":
        res = check_poem_style(check_function)
        if res != "成功":
            return res
        return res
    elif task_info == "请创作一篇小说......":
        res = check_noval_style(check_function)
        if res != "成功":
            return res
        return res
    elif task_info == "请评论你最近发生的一件事......":
        res = check_comments_style(check_function)
        if res != "成功":
            return res
        return res
    return "成功"

def common_style_check(check_function):
    # 这个函数就可以用来检查一些东西
    # 1. 字数是否达标
    word_num = check_function.check_text_num()
    if word_num < 20:
        return "字数未达到要求"
    # 2. 是否是乱打的
    res = check_function.check_logic()
    if res != "成功":
        return res
    else:
        return "成功"

def common_logic_check(check_function, task_related_words):
    for word in check_function.split_words_list:
        if word in task_related_words:
            return "成功"
    else:
        return "与主题不相关"

def check_poem_style(check_function):
    # 0. 判断句子数是否为偶数句
    sentence_num = check_function.check_sentences_num()
    if sentence_num % 2 != 0:
        return "诗句的句数有问题"
    # 1. 判断字数是否符合要求，如果不符合，返回“字符不符合诗歌的要求”
    word_num = check_function.check_text_num()
    if word_num < 24:
        return "字数未达到要求"
    # 2. 判断是否符合诗的格式
    res = check_function.check_rhyme()
    if not res:
        return "不满足诗歌韵脚"
    # 3. 判断是否每句话有逻辑：如果一句话都是分成了一个字一个字的，我就可以判断为是不符合逻辑的，因为中文没有词是不可能的
    res = check_function.check_logic()
    return res

def check_poem_logic(check_function, task_related_words):
    # 4. 判断是否符合主题
    for word in check_function.split_words_list:
        if word in task_related_words:
            return "成功"
    else:
        return "与主题不相关"

def check_noval_style(check_function):
    # 0. 判断句子数是否超过了十句
    sentence_num = check_function.check_sentences_num()
    if sentence_num < 10 or not sentence_num:
        return "句子数不达标"
    # 1. 判断字数是否符合要求，三百字
    word_num = check_function.check_text_num()
    if word_num < 300:
        return "字数未达到要求"

def check_noval_logic(check_function, task_related_words):
    # 4. 判断是否符合主题
    for word in check_function.split_words_list:
        if word in task_related_words:
            return "成功"
    else:
        return "与主题不相关"

def check_comments_style(check_function):
    # 0. 判断句子数是否超过了十句
    sentence_num = check_function.check_sentences_num(check_function.data)
    if sentence_num < 5:
        return "句子数不达标"
    # 1. 判断字数是否符合要求，三百字
    word_num = check_function.check_text_num()
    if word_num < 100:
        return "字数未达到要求"

