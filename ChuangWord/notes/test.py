import jieba

data = "我现在还想吃点东西，感觉肚子饿了。"
word_list = jieba.cut(data)
print(list(word_list))