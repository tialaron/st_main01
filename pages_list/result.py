import streamlit as st

def result_page():
    st.header("Ваши результаты 🏆")

    # Фиктивные данные, замените их на реальные данные из вашей системы
    total_tasks = 20
    completed_tasks = 15
    success_rate = (completed_tasks / total_tasks) * 100
    grade = 4.8
    certificates = ["Certificate of Completion - Track 1", "Certificate of Excellence - Track 2"]

    st.write(f"**Общее количество задач:** {total_tasks}")
    st.write(f"**Выполненных задач:** {completed_tasks}")
    st.write(f"**Процент выполненных задач:** {success_rate:.2f}%")
    st.write(f"**Ваша оценка:** {grade}")

    st.subheader("Сертификаты:")
    for cert in certificates:
        st.write(f"- {cert}")
