import streamlit as st
import pandas as pd

def map_page(df):
    st.header("Карта треков 🗺️")

    # Фильтры для датасета
    track_category = st.selectbox("Выберите категорию трека", df["Track_main"].unique())
    track_subcategory = st.selectbox("Выберите подкатегорию трека", df[df["Track_main"] == track_category]["Track"].unique())
    track_status = st.selectbox("Выберите статус трека", df["Status"].unique())

    # Фильтрация датасета
    filtered_df = df[(df["Track_main"] == track_category) & (df["Track"] == track_subcategory) & (df["Status"] == track_status)]

    # Отображение карточек для каждого трека
    for index, row in filtered_df.iterrows():
        st.subheader(row["Track"])
        st.markdown(f'<img src="https://github.com/Chetoff1228/images/blob/main/{row["Picture"]}.png?raw=true" alt="Foo" width="300" height="300"/></a>', unsafe_allow_html=True)
        st.write(f"**Статус:** {row['Status']}")
        st.write(f"**Имя:** {row['Name']}")
        st.write(f"**Источник:** {row['Source']}")
        st.write(f"**Ссылка:** {row['Caption']}")
        st.write("\n")