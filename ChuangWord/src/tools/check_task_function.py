import jieba
import pohan
from pohan.pinyin.pinyin import Style


class checkFunction():

    def __init__(self, work_edit_area, task_related_words):
        self.data = work_edit_area.toPlainText()
        self.word_list = list(jieba.cut(self.data))
        try:
            self.task_related_words = task_related_words.split("、")
        except:
            pass

    def check_sentences_num(self):
        self.half_sentence_list = []
        # 把文本按照“。”切分
        sentence_list = self.data.split("。")
        if len(sentence_list) <= 1:
            return None, None
        # 把句子按照“，”切分
        for sentence in sentence_list:
            sentences = sentence.split("，")
            for sentence in sentences:
                self.half_sentence_list.append(sentence)
        # 计算切分后的长度
        sentence_num = len(self.half_sentence_list)

        return self.half_sentence_list, sentence_num

    def check_text_num(self):
        word_num = len(self.data)
        return word_num

    def check_rhyme(self):
        last_rhyme_list = []
        for half_sentence in self.half_sentence_list:
            transfor_to_pinyin = pohan.pinyin.han2pinyin(half_sentence, style=Style.TONE3)
            last_word = transfor_to_pinyin[-1][0]
            last_rhyme = last_word[-1]
            last_rhyme_list.append(last_rhyme)
        for index, rhyme in enumerate(last_rhyme_list):
            if index + 1 == 1:
                continue
            if (index + 1) % 2 == 0:
                if rhyme != "1" or "2":
                    return False
            else:
                if rhyme != "3" or "4":
                    return False
        return True

    def check_logic(self):
        # todo 随便挑出一句话，看看是否满足主谓宾
        self.split_words_list = list(jieba.cut(self.data))
        for word in self.split_words_list:
            if len(word) > 1:
                return "成功"
        else:
            return "语言不合逻辑"