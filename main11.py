##　command + D で同じものを複数選択

import streamlit as st
import numpy as np 
import pandas as  pd

##サイドバーに追加


# テキストを打ち込める
st.write('Interractive Widgets')
opt = st.sidebar.text_input('あなたの趣味を教えてください。')
'あなたの趣味は', opt, 'です。'

# 動かせるスライドを表示させる
condision = st.sidebar.slider('あなたの今の調子は？', 0, 53, 50 )
'コンディション：', condision 

##２からむレイアウト
left_column, right_column= st.beta_columns(2)
button = left_column.button('右カラムに文字を表示')
if button:
    right_column.write('ここは右カラム')

## エキスパンダー　拡張
expandar=  st.beta_expander('問い合わせ１')
expandar.write('問い合わせ１の回答')
answer1 = st.text_input('さらなる質問はこちら')
answer1, 'こちらで間違い無いですか？'
expandar=  st.beta_expander('問い合わせ２')
expandar.write('問い合わせ2の回答')
expandar=  st.beta_expander('問い合わせ3')
expandar.write('問い合わせ3の回答')
expandar=  st.beta_expander('問い合わせ4')
expandar.write('問い合わせ4の回答')