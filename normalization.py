# -*- coding: utf-8 -*-
'''
@author: Leslie Pan
'''


import re
import jieba

#刑法分则的相对地址
law_dir = 'data/CriminalLaw.txt'
#停用词的相对地址
stopwords_dir = 'data/ChineseStopWords.txt'

def get_data(law_dir = law_dir):
    #先提取出条文的lines
    section_all = [token for token in open(law_dir, 'r').readlines() if re.match('^第.[章节]', token) is None]
    #合并lines，为之后的切分做准备
    section_all = ''.join(section_all)
    #将条文序号与条文内容切分开
    section_sp = re.split('(第.+条\s|第.+条之.\s)', section_all)
    #切分后位置0为空值，需要剔除
    section_sp = section_sp[1:]
    #消除换行符和空格
    section_sp = [token.replace('\n', '') for token in section_sp]
    section_sp = [token.replace(' ', '') for token in section_sp]
    return section_sp

def get_stopwords(stopword_dir = stopwords_dir):
    #以下词需要从停用词表中剔除
    stopwordexclude = ['一', '二', '三', '四', '五', '六', '七', '八', '九', '十']
    stopwords = [token.replace('\n', '') for token in open(stopword_dir, 'r', encoding='utf-8').readlines() if token not in stopwordexclude]
    return stopwords

def get_dict(data = get_data(), stopwords = get_stopwords()):
    #section_dict词典是为了保存条文序号与条文分词，为后面计算tfidf值做准备
    section_dict = {}
    for i in range(0, len(data), 2):
        section_dict[data[i]] = [token for token in jieba.cut(data[i + 1]) if token not in stopwords]
        
    #section词典是为了保存条文序号与完整的条文
    section = {}
    for i in range(0, len(data), 2):
        section[data[i]] = data[i + 1]
        
    return section_dict, section