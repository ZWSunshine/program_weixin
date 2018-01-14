# _*_coding:utf-8_*_
import jieba

# 读取文件内容
t1 = open("民生", encoding='utf-8', errors='ignore')
t2 = open("影评", encoding='utf-8', errors='ignore')

content1 = t1.read()
content2 = t2.read()

#print(content1)
#print(content2)

#jieba进行分词
data1 = jieba.cut(content1, encoding='utf-8')
data2 = jieba.cut(content2, encoding='utf-8')

print(data1,data2)