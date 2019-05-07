import pandas as pd
from sklearn.decomposition import NMF
from sklearn.preprocessing import Normalizer, MaxAbsScaler
from sklearn.pipeline import make_pipeline
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfVectorizer
import chardet

def find_encoding(fname):
    r_file = open(fname, 'rb').read()
    result = chardet.detect(r_file)
    charenc = result['encoding']
    return charenc


# my_encoding = find_encoding('xaa.csv')
# print(my_encoding)
file = pd.read_csv('songdb-clean-name.csv',encoding="utf-8")
#file = file.drop(['Votes','Director', 'Year','Metascore', 'Rating','Runtime (Minutes)','Revenue (Millions)'], axis=1)
file.head()

vectorizer = CountVectorizer()
vectorizer.fit(file['Lyric'])
X2= vectorizer.transform(file['Lyric'])
X2[0].shape

vectorizer = TfidfVectorizer()
vectorizer.fit(file['Lyric'])
X1 = vectorizer.transform(file['Lyric'])
X1[0].shape

scaler = MaxAbsScaler()
nmf = NMF(n_components=50)
normalizer = Normalizer()
pipeline = make_pipeline(scaler,nmf,normalizer)
norm_features1 = pipeline.fit_transform(X1)
norm_features2 = pipeline.fit_transform(X2)
df1 = pd.DataFrame(norm_features1,index=file['Lyric'])
df2 = pd.DataFrame(norm_features2,index=file['Lyric'])

df1Title = pd.DataFrame(norm_features1,index=file['Title'])
df2Title = pd.DataFrame(norm_features2,index=file['Title'])

def movieRelateContent(article,df,df2):
 article_index = df.loc[article]
 relateTitle = df2.dot(article_index)
 relateDesc = df.dot(article_index)
 print(relateTitle.nlargest())
 print('-------------------------------')
 print(relateDesc.nlargest())
 print('-------------------------------')
    
movieRelateContent('เพลง : กาลครั้งหนึ่งศิลปิน : ฟริคอัลบั้ม : Inside Outอาจดีเกินไปซะจนไม่กล้ารับมันจะเสกพรใดๆ ให้กันคงไร้ความหมายคนอย่างฉันแค่เดินบนดินก็ดีถมไปขอบคุณนะแต่ขอรับมันด้วยใจเท่านั้นพอเมื่อเธอแค่บินหลงทางมาจากฟ้าไกลอาจจะคิดว่าพบเจ้าชายที่เธอใฝ่ฝันตื่นได้แล้วฉันไม่ใช่คนที่เธอต้องการเกิดบนดินมีหรือจะบินได้นาน เธอก็คงรู้เธอเป็นถึงนางฟ้าแล้วดูสิฉันเป็นใครมีอะไรตรงไหนที่คู่ควรกับเธอบ้างไหมก็ไม่มี เราต่างกันแสนไกลช่วยรีบบินจากไปเสียที วันนี้นิทานมันจบแล้วก็รู้ฉันรู้ว่าเธอก็ยังรักกันแต่ว่าวันพรุ่งนี้ของเธอสำคัญกว่าไหมจบตรงนี้แม้มันจะทำให้เราเสียใจแต่สักวันเธอนั้นก็คงพบใครที่เขาดีพร้อมเธอเป็นถึงนางฟ้าแล้วดูสิฉันเป็นใครมีอะไรตรงไหนที่คู่ควรกับเธอบ้างไหมก็ไม่มี เราต่างกันแสนไกลช่วยรีบบินจากไปเสียที วันนี้นิทานมันจบแล้วเพราะชีวิตมันโหดร้าย ไม่เคยง่ายดายไม่เหมือนในนิทานเธอเป็นถึงนางฟ้าแล้วดูสิฉันเป็นใครมีอะไรตรงไหนที่คู่ควรกับเธอบ้างไหมก็ไม่มี เราต่างกันแสนไกลช่วยรีบบินจากไปเสียที วันนี้นิทานมันจบแล้วฉันไม่ใช่เจ้าชายที่เธอฝัน',df2,df2Title)