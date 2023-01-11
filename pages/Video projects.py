import requests
import streamlit as st
from streamlit_lottie import st_lottie
import yfinance as yf
import matplotlib.pyplot as plt
import pandas as pd
import datetime as dt
from Stocks import load_lottie_url

#assets
haken_YT = 'https://youtu.be/TXDCrBIod5M'
music_animation = load_lottie_url("https://assets5.lottiefiles.com/packages/lf20_euaveaxu.json")

#youtube Projects
with st.container():
    st.write("---")

    left_column, right_column = st.columns((2,1))

    with left_column:
        st.header(":guitar: Prog play")
        st.video(haken_YT)
    with right_column:
        st.write("Other musical endeavour:")
        st.write("")
        st.write(":video_camera: ", "[ Playthrough video ](https://youtu.be/30yExNPqMNI)")
        st.write(":notes:", "[ My band's album ](https://asphyxiatenepal.bandcamp.com/album/asphyxiate-self-titled-ep)")
        #st.write(":notes:", "[ The Album ](https://asphyxiatenepal.bandcamp.com/album/asphyxiate-self-titled-ep)")
        st.write("")
        st_lottie(music_animation, height = 300)
