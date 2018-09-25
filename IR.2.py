import os
import chardet
from nltk import word_tokenize


def get_encoding(file):
    # 二进制方式读取，获取字节数据，检测类型
    with open(file, 'rb') as f:
        return chardet.detect(f.read())['encoding']


data = []
path = 'C:\\Users\\hp\\PycharmProjects\\20news-18828\\'
files = os.listdir(path)
print(files)
for i in files:
    files1 = os.listdir(path + i)
    for p in files1:
        with open(path + i + "\\" + p, "rb") as file:
            decoding = get_encoding(path + i + "\\" + p)
            if not decoding == None:
                lines = file.readlines()
                for line in lines:
                    line = line.decode(decoding)
                    data.append(line)
print(data)

#
# data = []
# with open('C:\\Users\\hp\\PycharmProjects\\20news-18828\\alt.atheism\\51060', "rb") as file:
#     lines = file.readlines()
# decoding = get_encoding('C:\\Users\\hp\\PycharmProjects\\20news-18828\\alt.atheism\\51060')
# for line in lines:
#     line = line.decode(decoding)
#     data.append(line)

data1 = []
for j in data:
    if j != "\n":
        data1.append(j[:-1].split(','))

print(data1)

# print(data1)

data2 = [data[0] for data in data1]
# data2=[]
# for data in data1:
#     data2.append(data[0])
print(data2)

data3 = "".join(data2)
print(data3)

data4 = [data3]

from sklearn.feature_extraction.text import CountVectorizer

vectorizer = CountVectorizer()
vectorizer.fit(data4)
print(vectorizer.vocabulary_)

vector = vectorizer.transform(data4)

print(vector.shape)
print(type(vector))
print(vector.toarray())
