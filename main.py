import os.path

import numpy as np
import streamlit as st
import pandas as pd

from utils.load_ephys import kilosort3_loader

st.set_page_config(page_title='ks3-to-other', page_icon='〰',
                   initial_sidebar_state="auto")

st.set_option('deprecation.showPyplotGlobalUse', False)
reduce_header_height_style = """
    <style>
        div.block-container {padding-top:3rem;}
        div.block-container {padding-left:2rem;}
        div.block-container {padding-right:1rem;}
    </style>
"""
st.markdown(reduce_header_height_style, unsafe_allow_html=True)

st.title('kilosort + phy2 outputs into other readable formats')
