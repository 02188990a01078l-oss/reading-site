# -*- coding: utf-8 -*-
"""
Created on Fri Aug  7 21:40:03 2026

@author: dswda_uscxvt9
"""

import streamlit as st

def subject(df, su):
    if su == '첫사랑':
        st.write(df['첫사랑'])
    elif su == '짝사랑':
        st.write(df['짝사랑'])
    elif su == '재회':
        st.write(df['재회'])
    elif su == '금지된 사랑':
        st.write(df['금지된 사랑'])
    elif su == '절친':
        st.write(df['절친'])
    elif su == '배신':
        st.write(df['배신'])
    elif su == '치유':
        st.write(df['치유'])
    elif su == '트라우마':
        st.write(df['트라우마'])
    elif su == '청소년기':
        st.write(df['청소년기'])
    elif su == '복수':
        st.write(df['복수'])
    elif su == '용서':
        st.write(df['용서'])