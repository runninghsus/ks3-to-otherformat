import streamlit as st
import pandas as pd


@st.cache
def df_to_csv(df):
    # IMPORTANT: Cache the conversion to prevent computation on every rerun
    return df.to_csv().encode('utf-8')


# @st.cache
# def df_to_dict(df):
#     OutData = {}
#
#     # convert DF to dictionary before loading to your dictionary
#     OutData['Obj'] = df.to_dict('list')
#     return OutData
