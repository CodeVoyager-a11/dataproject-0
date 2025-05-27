import streamlit as st
import pandas as pd
import plotly.express as px

st.title("최근 5년간 KBO 리그 연간 관객수 변화")

# 예시 데이터 (2019~2023년 KBO 관객 수, 단위: 만 명)
data = {
    "연도": [2019, 2020, 2021, 2022, 2023],
    "관객수(만명)": [7_800, 2_400, 4_000, 5_300, 6_500]
}

df = pd.DataFrame(data)

# 막대 그래프 그리기
fig = px.bar(df, x="연도", y="관객수(만명)",
             labels={"관객수(만명)": "관객 수 (만 명)"},
             title="KBO 리그 연간 관객 수 (2019-2023)",
             text="관객수(만명)")

fig.update_traces(texttemplate='%{text:.2s}', textposition='outside')
fig.update_layout(yaxis=dict(range=[0, max(df["관객수(만명)"]) * 1.2]))

st.plotly_chart(fig, use_container_width=True)
