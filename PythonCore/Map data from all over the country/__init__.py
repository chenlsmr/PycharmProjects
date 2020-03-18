import pandas as pd
from wordcloud import WordCloud, ImageColorGenerator
import matplotlib.pyplot as plt
def draw_cloud(read_name):
    # 参数分别是指定字体、背景颜色、
    wc = WordCloud(font_path='simkai.ttf',
                   background_color="black",  # 背景颜色
                   )
    fp = pd.read_csv(read_name, encoding='utf-8')
    name = list(fp.city)  # 词
    value = fp.confirm  # 词的频率
    for i in range(len(name)):
        name[i] = str(name[i])
    dic = dict(zip(name, value))  # 词频以字典形式存储
    wc.generate_from_frequencies(dic)  # 根据给定词频生成词云
    plt.imshow(wc)
    plt.axis("off")  # 不显示坐标轴
    plt.show()
    wc.to_file('guangdong.png')  # 图片命名
if __name__ == '__main__':
    draw_cloud("guangdong.csv")