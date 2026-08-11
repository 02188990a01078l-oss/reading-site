# -*- coding: utf-8 -*-
"""
Created on Fri Aug  7 21:40:03 2026

@author: dswda_uscxvt9
"""

import streamlit as st

def subject(df, su):
    if su == '첫사랑':
        with st.expander("첫사랑 - 도윤과 하은", width=300):
            st.write(df.loc[0, '첫사랑'])
    elif su == '짝사랑':
        with st.expander("짝사랑 - 민재, 유진, 준우", width=300):
            st.write(df.loc[0, '짝사랑'])
    elif su == '재회':
        st.write("작품이 없습니다!\n")
    elif su == '금지된 사랑':
        with st.expander("금지된 사랑 - 이안과 세아"):
            st.write(df.loc[0, '금지된 사랑'])
    elif su == '절친':
        with st.expander("절친 - 태양과 시우"):
            st.write(df.loc[0, '절친'])
    elif su == '배신':
        with st.expander("배신 - 진호와 성민"):
            st.write(df.loc[0, '배신'])
    elif su == '치유':
        with st.expander("치유 - 지아와 윤재"):
            st.write(df.loc[0, '치유'])
    elif su == '트라우마':
        with st.expander("트라우마 - 민석과 주아"):
            st.write(df.loc[0, '트라우마'])
    elif su == '청소년기':
        with st.expander("청소년기 - 동화와 민주"):
            st.write(df.loc[0, '청소년기'])
    elif su == '복수':
        with st.expander("복수 - 강준과 도현"):
            st.write(df.loc[0, '복수'])
    elif su == '용서':
        st.write("작품이 없습니다!\n")
