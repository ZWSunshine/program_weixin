import codecs

from gensim import corpora

stop_words = '停用词'
stopwords = codecs.open(stop_words,'r',encoding='utf8').readlines()
stopwords = [ w.strip() for w in stopwords ]
stop_flag = ['x', 'c', 'u','d', 'p', 't', 'uj', 'm', 'f', 'r']

#分词，去停用词
def tokenization(filename):     #定义方法产生分词并去除停用词后所产生的列表
    result = []
    with open(filename, 'r') as f:
        text = f.read()
        words = jieba.cut(text)
    for word, flag in words:
        if flag not in stop_flag and word not in stopwords:
            result.append(word)
    return result

filenames = ['影评',
             '民生',
             '中国关键词'
            ]
corpus = []
for each in filenames:
    corpus.append(tokenization(each))
print (len(corpus))

dictionary = corpora.Dictionary(corpus)
print (dictionary)






