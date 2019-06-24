# -*- coding: utf-8 -*-
'''
@author: Leslie Pan
'''


import math

#该方法为计算idf值，需要先统计单词出现过条文的条文数
def get_idfdict(section_dict):
    #统计每个词在分则中出现的条文数量
    word_dict = {}
    for word_list in section_dict.values():
        for word in set(word_list):
            if word in word_dict.keys():
                word_dict[word] += 1
            else:
                word_dict[word] = 1
                
    #总条文数
    tt_count = len(word_dict.keys())
    
    #计算各个单词的idf值，使用拉普拉斯平滑
    idf_dict = {}
    for k, v in word_dict.items():
        idf_dict[k] = math.log(tt_count/(1.0 + v))
        
    return idf_dict

#该方法统计单词在每条条文中出现的频率
def get_tfdict(section_dict):
    tf_dict = {}
    for k, word_list in section_dict.items():
        d = {}
        for word in word_list:
            #需要统计词频率，但字典包含字典不好操作，所以直接除以常数条文的词总数
            c = len(word_list)
            if word in d.keys():
                d[word] += 1 / c
            else:
                d[word] = 1 / c
        tf_dict[k] = d 
    
    return tf_dict

#该方法以tf的词典为基础，主要是考虑到无需储存没出现的单词，计算tfidf值
def get_tfidfdict(section_dict):
    idf_dict = get_idfdict(section_dict)
    tf_dict = get_tfdict(section_dict)
    tfidf_dict = {}
    for k, tf in tf_dict.items():
        d = {}
        for word, num in tf.items():
            d[word] = num / idf_dict[word]
        tfidf_dict[k] = d
        
    return tfidf_dict