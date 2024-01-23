import pandas as pd
from io import BytesIO
import requests

import streamlit as st
from streamlit_option_menu import option_menu

from pages_list import *

r = requests.get('https://docs.google.com/spreadsheet/ccc?key=1ePOZXadY5GG1L7yXrfSgNpa-JKeeHgfrYYogdDVTi2k&output=csv')
df_search = pd.read_csv(BytesIO(r.content), index_col=0)

# Заголовок страницы
st.set_page_config(page_title="Лаборатория цифровых компетенций", page_icon="👾", layout="wide")

with st.sidebar:
    redirect_url = "http://83.143.66.61:27369/"
    logo_image = 'https://raw.githubusercontent.com/Chetoff1228/images/main/logo.png'
    st.markdown(f'<a href="{redirect_url}"><img src="{logo_image}" alt="Foo" width="150" height="150"/></a>', unsafe_allow_html=True)
  
with st.sidebar:
    selected = option_menu('', ["🏠 Старт", "👨🏻‍💻 Личный кабинет", '🗺️ Карта треков','🏆 Успехи', '📜 Правила прохождения курсов'])

if selected == "🏠 Старт":
    main_page(df_search)
elif selected == "👨🏻‍💻 Личный кабинет":
    lk_page()
elif selected == "🗺️ Карта треков":
    map_page(df_search)
elif selected == "🏆 Успехи":
    result_page()
else:
    rules_page()

