# coding:utf-8
import jieba.posseg


def bjx():
    """
    使用百家姓过滤掉，不在百家姓之间的实体
    :return:
    """
    bjx = open("bjx.txt", "r", encoding="utf-8")
    name = open("entity.txt", "r", encoding="utf-8")
    final_name = open("entity1.txt", "w", encoding="utf-8")
    UN_final_name = open("un_entity.txt", "w", encoding="utf-8")
    content = bjx.read()
    str = ""
    for sentence in content:
        str = str + sentence.strip() + " "
    for entity in name.readlines():
        entity = entity.strip()
        if entity[0] in str or entity[:1] in str:
            if len(entity) > 1:
                final_name.write(entity)
                final_name.write("\n")
        else:
            UN_final_name.write(entity)
            UN_final_name.write("\n")


def cixing():
    """
    使用词性分析实体中的词性
    :return:
    """
    entity = open("entity1.txt", "r", encoding="utf-8")
    names = entity.readlines()
    for name in names:
        for word in list(name):
            list1 = jieba.posseg.lcut(word)
            for i in list1:
                print(i)


def rm_dup():
    """
    删除前缀重复的实体
    :return:
    """
    entity = open("entity1.txt", "r", encoding="utf-8")
    write_file = open("entity2.txt", "w", encoding="utf-8")
    entity = entity.readlines()
    words = set()
    for name in entity:
        if name.strip() not in words and len(name.strip()) == 2:
            words.add(name.strip())
    for names in entity:
        if len(names.strip()) == 2:
            write_file.write(names.strip())
            write_file.write("\n")
        if names.strip()[:2] not in words and len(names.strip()) > 2:
            write_file.write(names.strip())
            write_file.write("\n")


def located():
    """
    定位 位置
    :return:
    """
    file = open("entity2.txt", "r", encoding="utf-8")
    words = file.readlines()
    article = open("shz.txt", "r", encoding="utf-8")
    content = article.read()
    sentences = content.split("。")
    for sentence in sentences:
        seg_list = jieba.posseg.lcut(sentence)
        count = 0
        for i in seg_list:

            if i.flag == "nr" and i.word + "\n" in words:
                count += 1
                if count == 2:
                    print(sentence)



if __name__ == '__main__':
    located()



