import  os
from google.cloud import texttospeech

import io 
import streamlit as st
from streamlit.elements.color_picker import ColorPickerMixin


os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = 'secret.json'



from google.cloud import texttospeech
from IPython.display import Audio

def synthesize_speech(text, lang ='日本語',gender= 'default'):
    gender_type = {
        'default':texttospeech.SsmlVoiceGender.SSML_VOICE_GENDER_UNSPECIFIED,
        'male' : texttospeech.SsmlVoiceGender.MALE,
        'female':texttospeech.SsmlVoiceGender.FEMALE,
        'neautral':texttospeech.SsmlVoiceGender.NEUTRAL
    }

    lang_code = {
        '英語やで？ええん？ほんまに？わかる？':'en-US',
        '日本語':'ja-JP'
    }


  
    client = texttospeech.TextToSpeechClient()

    synthesis_input = texttospeech.SynthesisInput(text=text)


    voice = texttospeech.VoiceSelectionParams(
        language_code=lang_code[lang], ssml_gender=gender_type[gender]
    )

    audio_config = texttospeech.AudioConfig(
        audio_encoding=texttospeech.AudioEncoding.MP3
    )


    response = client.synthesize_speech(
        input=synthesis_input, voice=voice, audio_config=audio_config

    )
    return response

    
st.title('音声出力アプリ,いわゆる棒読みちゃんやで')

st.markdown('###  データ準備したるで')
input_option = st.selectbox(
    '入力データの選択',
    ('直接入力する？？','テキストファイルもっとるん自分？.txtのやつやで？')
)
input_data = None

if input_option  == '直接入力する？？':
    input_data = st.text_area('ここに読んで欲しい文書けよ！！。','ここに早よかけ言うてるやん！！！そうじゃないとこの文読むで？ええんか？')
else:
    uploaded_file = st.file_uploader('テキストファイルもっとるん自分？.txtのやつやで？',['txt'])
    if uploaded_file is not None:
        content = uploaded_file.read()
        input_data = content.decode()

if input_data is not None:
    st.write('これでええか？')
    st.write(input_data)
    st.markdown('###  パラメーター設定')
    st.subheader(('言語と話者の性別選択'))

    lang = st.selectbox(
        '言語を選択しろやぼけええええ',
        ('日本語','英語やで？ええん？ほんまに？わかる？')

    )
    gender = st.selectbox(
        '話者の性別を選択しろやぼけええええ',
        ('default','male','female','neutral')
    )
    st.markdown('### 音声合成')
    st.write('しゃーない読んだるから耳の穴かっぽじってよー聞けよ？ほなここ押してみ！！',  Color= 'orange')
    if st.button('しゃーない読んだるから耳の穴かっぽじってよー聞けよ？ほなここ押してみ！！'):
        comment = st.empty()
        comment.write('音声出力を開始するで？ええな？')
        response = synthesize_speech(input_data, lang, gender=gender)
        st.audio(response.audio_content)
        comment.write('完了したで。感謝せえよ？')
    