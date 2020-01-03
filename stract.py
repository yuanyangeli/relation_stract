# coding:utf-8
# 使用正则表达式抽取人物关系语句

import re
import jieba.posseg
write_open = open("entity.txt", "w", encoding="utf-8")
file = open("shz.txt", "r", encoding="utf-8")
content = file.read()
sentences = content.split("。")
name = []
for sentence in sentences:
    word = jieba.posseg.cut(sentence)

    l = []
    for i in word:
        l.append((i.word, i.flag))
    for split_sentence in l:
            if split_sentence[1] in ["nr"]:
                name.append(split_sentence[0])
name = set(name)
print(name)
print(len(name))
for en in  name:
    write_open.write(en)
    write_open.write("\n")
    # p = re.compile("[\u4e00-\u9fa5]*是[\u4e00-\u9fa5]*")
    # q = re.compile("[\u4e00-\u9fa5]*和[\u4e00-\u9fa5]*")
    # result = re.search(p, sentence)
    # result1 = re.search(q, sentence)
    # if result != None:
    #     print(result)
    # if result1 != None:
    #     print(result1)



