from wordcloud import WordCloud
import matplotlib.pyplot as plt
from collections import Counter
from konlpy.tag import Okt
from PIL import Image
import numpy as np

print('hello world!!')

with open('잡스스탠포드연설.txt', 'r', encoding='utf-8') as f:
    text = f.read()

okt = Okt()
nouns = okt.nouns(text) # 명사만 추출
# print(nouns)
words = [n for n in nouns if len(n) > 1] # 단어의 길이가 1개인 것은 제외
# print(words)
c = Counter(words) # 위에서 얻은 words를 처리하여 단어별 빈도수 형태의 딕셔너리 데이터를 구함
# print(c)
img = Image.open('애플마스크.jpg')
img_array = np.array(img)
wc = WordCloud(font_path='./NanumGothic.ttf', width=400, height=400, scale=2.0, max_font_size=250, mask=img_array)
gen = wc.generate_from_frequencies(c)
# plt.figure()
# plt.imshow(gen)
wc.to_file('잡스연설_워드클라우드.png')