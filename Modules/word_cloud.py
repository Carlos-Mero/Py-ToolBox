import docx
import re
import jieba
import collections
import wordcloud
import matplotlib.pyplot as plt
wordtextfinal=[]


def getword(path):
    file = docx.Document(path)
    wordlist = []
    for i in file.paragraphs:
        wordlist.append(i.text)
    return wordlist


def main(doc_path, FontPath = 'Hiragino Sans GB'):
    wordlist = getword(doc_path)
    wordlist = "".join(wordlist)
    wordlist = re.sub('[^\u4e00-\u9fa5]+', '', wordlist)
    wordlist = "".join(wordlist)
    wordlist = jieba.lcut(wordlist, cut_all=False, HMM=True)
    stopwords = [line.strip() for line in open('停用词库.txt', 'r', encoding='utf-8').readlines()]
    for word in wordlist:
        if word not in stopwords:
            wordtextfinal.append(word)
    wordcounts = collections.Counter(wordtextfinal)
    #wordcounts_top = wordcounts.most_common(30)
    wc = wordcloud.WordCloud(
        font_path=FontPath,
        background_color='white',
        max_words=20,
        max_font_size=150
)
    wc.generate_from_frequencies(wordcounts)
    plt.figure('词云')
    plt.imshow(wc, cmap=plt.cm.gray, interpolation='bilinear')
    plt.axis('off')
    plt.show()
    return 0

if __name__ == "__main__":
    main(None, None)