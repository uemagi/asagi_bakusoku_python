import streamlit as st
import numpy as np 
import pandas as  pd


st.title('Streamlit 超入門 10')

# インタラクティブウィジェッツ　https://docs.streamlit.io/en/stable/api.html#display-interactive-widgets

#　画像表示 https://docs.streamlit.io/en/stable/api.html#display-media
from PIL import Image
st.write('Display Image')

## 写真 チェックボックスにクリックしたら表示させる
if st.checkbox('Show Image'):
    img = Image.open('証明写真.jpg')
    st.image(img, caption='Asagi Ueda', use_column_width=True)

# すきな数字を選択できる
option = st.selectbox(
    'あなたが好きな数字を教えてください、',
    list(range(1,11 ))
)
'あなたの好きな数字は、', option, 'です。'

# テキストを打ち込める
st.write('Interractive Widgets')
opt = st.text_input('あなたの趣味を教えてください。')
'あなたの趣味は', opt, 'です。'

# 動かせるスライドを表示させる
condision = st.slider('あなたの今の調子は？', 0, 53, 50 )
'コンディション：', condision 