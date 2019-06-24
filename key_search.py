# -*- coding: utf-8 -*-
'''
@author: Leslie Pan
'''

import jieba
import pandas as pd
import normalization
import tf_idf

#输入关键字方法
def input_str():
    r = input('请输入搜索关键词句：')
    if r == '':
        r = '贩卖儿童'
    return r

#查找含关键字的条文，并按tfidf值大小排序返回
def get_df(search_sentence, tfidf_dict):
    df = pd.DataFrame(columns = ['Section', 'TF-IDF'])
    indx = 0
    for k, word_tfidf in tfidf_dict.items():
        t_values = 0
        for i in jieba.cut(search_sentence):
            if i in word_tfidf.keys():
                t_values += word_tfidf[i]
        if t_values > 0:
            df.loc[indx] = [k, t_values]
        indx += 1
    df = df.sort_values(by = 'TF-IDF', ascending = False)
    
    return df

#打印匹配后的结果
def print_recall(recall_df, section, limit_num = 5):
    if len(recall_df) < 1:
        print('对不起，无搜索结果！')
    else:
        df = recall_df.head(limit_num)
        for i in range(len(df)):
            print(df.iloc[i][0], section[df.iloc[i][0]])
            print('---------------------------------------------')
            
def main():
    section_dict, section = normalization.get_dict()
    tfidf_dict = tf_idf.get_tfidfdict(section_dict)
    print('中国刑法已经学习完毕')
    keywords = input_str()
    recall_df = get_df(keywords, tfidf_dict)
    print('你要搜索的关键词句是：', keywords)
    print_recall(recall_df=recall_df, section = section, limit_num = 5)
    
if __name__ == "__main__":
    main()