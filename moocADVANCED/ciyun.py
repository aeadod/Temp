import jieba
import wordcloud
from scipy.misc import imread
mask=imread('b.png')
f=open(r"C:\Users\aeado\Desktop\baogao.txt",'r',encoding='gb18030')
t=f.read()
f.close()
ls=jieba.lcut(t)
txt=' '.join(ls)
w=wordcloud.WordCloud(mask=mask,max_words=2000,font_path='msyh.ttc',width=1000,height=700,background_color='white')
w.generate(txt)
w.to_file('grow2.png')
