import streamlit as st
import pandas as pd
import plotly.express as px

st.title("최근 5년간 KBO 리그 연간 관객수 변화")

data = {
    "연도": [2019, 2020, 2021, 2022, 2023],
    "관객수(만명)": [780, 240, 400, 530, 650]
}
df = pd.DataFrame(data)

source = st.text_input("📖 데이터 출처를 입력하세요:", "KBO 공식 홈페이지")

fig = px.line(
    df,
    x="연도",
    y="관객수(만명)",
    markers=True,
    title="KBO 리그 연간 관객 수 (2019-2023)",
    labels={"관객수(만명)": "관객 수 (만 명)", "연도": "연도"}
)

fig.update_layout(
    yaxis=dict(range=[0, max(df["관객수(만명)"]) * 1.2]),
    xaxis=dict(tickmode='linear', dtick=1)  # x축 눈금을 1단위 정수로 설정
)

st.plotly_chart(fig, use_container_width=True)

st.markdown(f"<p style='font-size:0.8em; color:gray;'>출처: {source}</p>", unsafe_allow_html=True)
