import streamlit as st
import pandas as pd
import plotly.graph_objs as go

st.title("최근 10년간 KBO 리그 연간 관객수 변화")

# 예시 데이터 (2014~2023년, 단위: 만 명)
data = {
    "연도": list(range(2014, 2024)),
    "관객수(만명)": [650, 700, 720, 740, 800, 780, 240, 400, 530, 650]
}

df = pd.DataFrame(data)

source = st.text_input("📖 데이터 출처를 입력하세요:", "KBO 공식 홈페이지")

# 최대/최소 관객수와 연도 찾기
max_idx = df['관객수(만명)'].idxmax()
min_idx = df['관객수(만명)'].idxmin()

# 선 그래프 만들기 (전체 회색 선)
fig = go.Figure()

fig.add_trace(go.Scatter(
    x=df['연도'],
    y=df['관객수(만명)'],
    mode='lines+markers',
    name='관객수',
    line=dict(color='gray'),
    marker=dict(color='gray', size=8)
))

# 최대값 포인트 빨간색으로 덮기
fig.add_trace(go.Scatter(
    x=[df.loc[max_idx, '연도']],
    y=[df.loc[max_idx, '관객수(만명)']],
    mode='markers',
    name='최대 관객수',
    marker=dict(color='red', size=12, symbol='circle')
))

# 최소값 포인트 파란색으로 덮기
fig.add_trace(go.Scatter(
    x=[df.loc[min_idx, '연도']],
    y=[df.loc[min_idx, '관객수(만명)']],
    mode='markers',
    name='최소 관객수',
    marker=dict(color='blue', size=12, symbol='circle')
))

fig.update_layout(
    title="KBO 리그 연간 관객 수 (2014-2023)",
    xaxis_title="연도",
    yaxis_title="관객 수 (만 명)",
    xaxis=dict(tickmode='linear', dtick=1),
    yaxis=dict(range=[0, max(df["관객수(만명)"]) * 1.2]),
    hovermode="x unified"
)

st.plotly_chart(fig, use_container_width=True)

st.markdown(f"<p style='font-size:0.8em; color:gray;'>출처: {source}</p>", unsafe_allow_html=True)
