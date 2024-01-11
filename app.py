import streamlit as st
import requests
import pynytimes
from pynytimes import NYTAPI
import datetime as datetime

client = nyt = NYTAPI("Y0DAWCyuEbgqltw3GnAUSA1EpuersHGv", parse_dates=True)


def complete_top_stories():
    formatted_date = top_stories_result['published_date'].strftime('%m-%d-%Y')
    summary = top_stories_result['abstract']
    creator = top_stories_result['byline']
    st.write(top_stories_result['title'])
    st.write(f"Date Published: {formatted_date}")
    st.write(f"Published {creator}")
    st.write(f"Summary of Article:\n{summary}")
    st.write(f"URL: {top_url}")
    
    
    
def complete_most_shared():
    formatted_date = most_shared_result['published_date'].strftime('%m-%d-%Y')
    summary = most_shared_result['abstract']
    creator = most_shared_result['byline']
    st.write(most_shared_result['title'])
    st.write(f"Date Published: {formatted_date}")
    st.write(f"Published {creator}")
    st.write(f"Summary of Article:\n{summary}")
    st.write(f"URL: {most_url}")


def complete_recent_published():
    formatted_date = recent_published_result['published_date'].strftime('%m-%d-%Y')
    summary = recent_published_result['abstract']
    creator = recent_published_result['byline']
    st.write(recent_published_result['title'])
    st.write(f"Date Published: {formatted_date}")
    st.write(f"Published {creator}")
    st.write(f"Summary of Article:\n{summary}")
    st.write(f"URL: {recent_url}")
    
def article_day_complete_published():
    formatted_date = article_of_day_result['published_date'].strftime('%m-%d-%Y')
    summary = article_of_day_result['abstract']
    creator = article_of_day_result['byline']
    st.write(article_of_day_result['title'])
    st.write(f"Date Published: {formatted_date}")
    st.write(f"Published {creator}")
    st.write(f"Summary of Article:\n{summary}")
    st.write(f"URL: {article_url}")



most_shared = nyt.most_shared()
recent_published = nyt.latest_articles()
top_stories = nyt.top_stories()
articleday = nyt.most_viewed()

top_stories_result = top_stories[0]
most_shared_result = most_shared[0]
recent_published_result = recent_published[0]
article_of_day_result = articleday[0]


top_url = top_stories_result['url']
most_url = most_shared_result['url']
recent_url = recent_published_result['url']
article_url = article_of_day_result['url']


st.title('The New York Times API')
st.header('Implemented into Streamlit by Kaartik Bhatia')

news_type = st.selectbox(
   "Select what type of News Article you would like to view.",
   ("Most shared articles", "Recently Published", "Top stories", "Article of the day")
)

st.write(f'You selected:', str(news_type))

if news_type == 'Most shared articles':
    complete_most_shared()
    
elif news_type == 'Recently Published':
    complete_recent_published()
    
elif news_type == 'Top stories':
    complete_top_stories()
    
elif news_type == 'Article of the day':
    article_day_complete_published()