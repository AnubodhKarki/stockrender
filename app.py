import requests
import streamlit as st
from streamlit_lottie import st_lottie
import yfinance as yf
import matplotlib.pyplot as plt
import pandas as pd
import plotly.graph_objects as go
from datetime import date, datetime, timedelta
 
st.set_page_config(page_title="Anub", page_icon=":globe_with_meridians:", layout="wide")
st.sidebar.success(":point_up_2: Select a page above")

#Retrive animation
def load_lottie_url(url):
    r = requests.get(url)
    if r.status_code !=200:
        return None
    return r.json()

#use local CSS
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

local_css('style/style.css')

#--load assets--
#animation
chart_animation = load_lottie_url("https://assets8.lottiefiles.com/packages/lf20_iqfq0ogz.json")

latest_date = date.today()
past_date= latest_date - timedelta(days=30)

#Header 

#st.title("Anub's dashboard for stock insights [U.S.]")
try:
    with st.container():

        left_column, right_column = st.columns(2)
        
        #---header section
        with left_column:

            st.subheader(":chart_with_upwards_trend: Asset panel :chart_with_downwards_trend:")
            st.title("Stock insights")
            st.subheader("NYSE | Nasdaq")

        with right_column:
            #latest_date
            st_lottie(chart_animation, height = 300, key ="coding", speed=1.3)        

    #chart and news
    with st.container():

        ticker = st.text_input("Enter stock ticker to get its data", "AMZN")
        left_column, right_column = st.columns(2)

        #---header section
        with left_column:
            st.write("Chart")
            # Get the data for the stock Apple by specifying the stock ticker, start date, and end date
            data = yf.download(ticker)
            df = pd.DataFrame(data)
            yf_dataframe = df["Open"]
            st.line_chart(yf_dataframe)
            #st.bar_chart(yf_dataframe)

        with right_column:
            st.write("Latest News 📰")
            news_ticker = yf.Ticker(ticker)
            news = news_ticker.news
            df = pd.DataFrame(news)

            df['published'] =  pd.to_datetime(df["providerPublishTime"], unit="s").dt.strftime("%Y-%m-%d")
            df_index = df.set_index(df['published'])
            df_index[['title','publisher', 'link']]
            
            #Make news Hyperlink
            # Generate a Markdown link for each row in the dataframe        
            #df["title"] = df.apply(lambda row: f"[{row['title']}]({row['link']})", axis=1)
            # Display the dataframe with the Markdown links
            #st.write(df[['published', 'publisher', 'title']])

    # Add a spacer with a height of 100 pixels

    with st.container():

        left_column, right_column = st.columns(2)
        
        with left_column:
            st.write("Stock Grade 🤔")
            ticker_recommendation = (yf.Ticker(ticker)).recommendations
            df_recommendation = pd.DataFrame(ticker_recommendation)
            df_recommendation.index= df_recommendation.index.strftime("%Y-%m-%d")
            #df_recommendation = df_recommendation.reset_index()

            #df_sorted = df_recommendation("date", ascending=False)

            #Sorting latest by reversing
            df_sorted = df_recommendation.iloc[::-1]
            df_sorted

            #Print recommendation from past to latest date
            #ticker_recommendation.loc[past_date:latest_date]

        with right_column:
            st.write("Financials 🧐")
            ticker_data = (yf.Ticker(ticker)).info
            ticker_financials = ["sector", "marketCap", "shortRatio", "grossProfits", "freeCashflow", "totalCash", "totalDebt", "ebitda", "trailingPE", "priceToBook",]

            #Constructing new dict with only wanted strings
            filtered_dict = {key: ticker_data[key] for key in ticker_financials if key in ticker_data}
            filtered_dict

    #Business Summary
except:
    st.write("Data unavailable!")