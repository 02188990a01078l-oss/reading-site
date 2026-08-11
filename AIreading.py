# -*- coding: utf-8 -*-
"""
Created on Fri Aug  7 20:04:42 2026

@author: dswda_uscxvt9
"""

import streamlit as st
import pandas as pd
import reading as r

st.title("📖 AI 스토리")
st.markdown("이 사이트는 AI로 생성한 다양한 장르의 스토리북을 볼 수 있습니다!\n")
st.markdown("* 차후에 스토리 작성 기능을 추가할 예정입니다!\n")
df = pd.read_excel("story.xlsx")
Sub_select = st.selectbox("주제 선택", ['첫사랑', '짝사랑', '재회', '금지된 사랑', '절친', '배신', '치유',
                                    '트라우마', '청소년기', '복수', '용서'])

if st.button("AI 스토리", icon="📑", icon_position="left", width="stretch"):
    r.subject(df, Sub_select)
    if st.button("홈으로~", icon="🛖", icon_position="left", width="content"):
        st.rerun()
            
st.write("\n")
st.write("\n")
st.markdown("📚 다양한 스토리북을 확인해보세요!\n")

st1, st2 = st.columns(2)
with st1:
    with st.expander("금지된 사랑 - 이안과 세아", width=300):
        st.write(df.loc[0, '금지된 사랑'])
with st2:
    with st.expander("복수 - 강준과 도현", width=300):
        st.write(df.loc[0, '복수'])
