import streamlit as st
import pandas as pd
import plotly.express as px

st.title("최근 5년간 KBO 리그 연간 관객수 변화")

# 예시 데이터 (단위: 만명)
data = {
    "연도": [2019, 2020, 2021, 2022, 2023],
    "관객수(만명)": [780, 240, 400, 530, 650]
}

df = pd.DataFrame(data)

# 출처 입력 칸
source = st.text_input("📖 데이터 출처를 입력하세요:", "KBO 공식 홈페이지")  # 기본값 설정 가능

# 선 그래프 생성
fig = px.line(
    df,
    x="연도",
    y="관객수(만명)",
    markers=True,
    title="KBO 리그 연간 관객 수 (2019-2023)",
    labels={"관객수(만명)": "관객 수 (만 명)", "연도": "연도"}
)

fig.update_layout(yaxis=dict(range=[0, max(df["관객수(만명)"]) * 1.2]))

# 그래프 출력
st.plotly_chart(fig, use_container_width=True)

# 출처 표시 (그래프 바로 아래에 주석처럼)
st.markdown(f"<p style='font-size:0.8em; color:gray;'>출처: {source}</p>", unsafe_allow_html=True)
