import jieba
filename = "国务院关于实施乡村振兴战略的意见.txt"
stopwords_file = "停用词.txt"

f = open(filename,"r",encoding="utf-8")
content = f.read()
f.close()

stop_f = open(stopwords_file,"r",encoding='utf-8')
stop_words = []
for line in stop_f.readlines():
    line = line.strip()
    if len(line) == 0:
        continue
    stop_words.append(line)
stop_f.close

def m_cut(intxt):
    return [ w for w in jieba.lcut(intxt) if w not in stop_words]
ls=m_cut(content)
word_list=[w for w in ls if len(w)>1]

#统计词语频率
from collections import Counter
word_frequency = Counter(word_list)

#生成词云
import matplotlib.pyplot as plt #可视化
from wordcloud import WordCloud

wordcloud = WordCloud(
    width=800,             # 图片宽度
    height=400,            # 图片高度
    background_color='white',  # 背景颜色
    colormap='viridis',    # 颜色风格
    max_words=200,         # 最大显示词数
    max_font_size=100,     # 最大字体尺寸
    font_path='msyh.ttc'  # 字体文件
).fit_words(word_frequency)

plt.imshow(wordcloud)
plt.axis("off")
plt.show()    

