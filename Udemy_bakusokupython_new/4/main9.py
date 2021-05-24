from re import T
import streamlit as st
import numpy as np 
import pandas as  pd

st.title('Streamlit A超入門')

st.write('DataFrame')

df = pd.DataFrame({
    '１列目':[1,2,3,4],
    '2列目':[10,20,30,40]

})

st.write(df)
st.dataframe(df)
st.dataframe(df, width=100, height=100) ##dataframeだと、大きさを指定できる。
st.dataframe(df, width=100, height=100) ##dataframeだと、大きさを指定できる。
st.dataframe(df.style.highlight_max(axis=0))##　列は０　行は１を指定してあげる
st.table(df.style.highlight_max(axis=0))
## https://docs.streamlit.io/en/stable/api.html#display-data にしっかりとかいてある

"""
# 章
## 節
### 項
```python
import streamlit as st
import numpy as np 
import pandas as  pd
```
"""## マークダウン　https://docs.streamlit.io/en/stable/api.html#display-text

#　グラフ　　https://docs.streamlit.io/en/stable/api.html#display-charts
dr = pd.DataFrame(
    np.random.rand(20, 3),
    columns=['a', 'b', 'c']
)
st.line_chart(dr)#　折れ線グラフ
st.area_chart(dr)#　塗り潰しグラフ
st.bar_chart(dr)#　棒グラフ

#　地図のマッピング
ds = pd.DataFrame(
    np.random.rand(100, 2)/[50,50] + [35.69, 139.70],
    columns=['lat', 'lon']
)
st.map(ds)

#　画像表示 https://docs.streamlit.io/en/stable/api.html#display-media
from PIL import Image
st.write('Display Image')

## 写真
img = Image.open('証明写真.jpg')
st.image(img, caption='Asagi Ueda', use_column_width=True)
##　動画
video_file = open('IMG_0306 2.mp4','rb')
video_bytes = video_file.read()
st.video(video_bytes)
