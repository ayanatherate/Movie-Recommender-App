import pandas as pd
import numpy as np
import streamlit as st
import time
import requests
import pandas as pd
from bs4 import BeautifulSoup
import re


st.set_page_config(page_title='Movie Recommendation App', page_icon="https://cdn-icons-png.flaticon.com/512/1038/1038100.png", layout="centered", initial_sidebar_state="auto", menu_items=None)
hide_streamlit_style2= '''
<style>
#MainMenu {visibility: hidden;}
footer {visibility: hidden;}
header {visibility: hidden;}
.css-1rs6os {visibility: hidden;}
.css-17ziqus {visibility: hidden;}
</style>

'''
st.markdown(hide_streamlit_style2, unsafe_allow_html=True) 


page_bg_img = '''
<style>
.stApp {
background-image: url("https://i.ibb.co/t869zV7/istockphoto-1124347647-170667a.jpg");
background-size: cover;
}
</style>
'''
st.markdown(page_bg_img, unsafe_allow_html=True)
st.title('Movies Recommender')
st.subheader('Let AI decide for you, what to watch next!')

def take_inp():
    inp=st.text_input(label='Enter a movie name, you just watched:')
    num_movies=st.select_slider('Select number of recommendations you want',options=[i for i in range(16)])
    inp=inp.lower()
    inp=re.sub('[^a-zA-Z0-9 ]','',inp)
    return inp,num_movies



data=pd.read_csv(r"https://raw.githubusercontent.com/ayanatherate/World-Movies-RecommendationSystem-and-Visualization/main/Recommendation_Database/Recommendations_data.csv")

#print(data['recommendaions'])

match_names=[data['normalized_names'][i] for i in range(len(data))]

def map_names(name):
    movie_index=''
    
    for i in range(len(match_names)):
        if name==match_names[i]:
            movie_index=i
            break        
    return movie_index

inp,num_movies=take_inp()

if len(inp)==0 and num_movies==0:
    st.stop()
else:
    movie_index_=map_names(inp)

recommendation=[]

try:
    for i in data['recommendaions'][movie_index_].split(','):
        recommendation.append(int(i))
except:
    st.write('Oops! Seems like this movie is not listed on our Database. You can also try checking out the official name of the movie from Google and try again!')
    st.stop()
    
st.caption('Here are your recommended movie lists:')   
num_made_recommends=0


for i in recommendation:
    if num_made_recommends<num_movies:
        temp= data[data['id']==i]
        st.write('----------------------')
        time.sleep(1)
        st.write(temp['title'].values[0])
        
        #scraping from tmdb web
        to_search_str='+'.join(temp['title'].values[0].split(' '))
        url=f'https://www.themoviedb.org/search?query={to_search_str}'
        r=requests.get(url)
        src=r.content
        soup = BeautifulSoup(src, 'lxml')
        thumb = soup.find("img", class_ = "poster")
        imgurl=thumb['src']
        imgurl='https://themoviedb.org/'+imgurl
        
        st.image(imgurl)
        #st.image+AGb32huPHb/Rqp9MNlepMh9knnP96o3cjxsdykMvDKfz5VXll8wpeWVAQWgy0OVptOj3n20JRs+nH9MVKtW8SxR7VXGSTxX2sVlHO4iWUDIBKnK5qjc6Pp1zO01xYwSSuu1nZASR8a0c18dlRGZvqqM5od/DaDSWVjZ3bxWsEUCDA2ouM1ptphNgyqAJgxdD/aq+iwi5vJbphkFs5NaOt30mn2El3FD4qxDc6g87fMj89s0dtPXReOPtL/AEpWMi31iCvJA2stcBBcxZWFQVzkb/KsPS9VNuwvIjuif94oGPnii2012zniDRtG3xPIrcmSpQbRQhs3kl3zjLfyjtXTUrlLOHZuG48sfSvOrdSWNlEWeVQfIDuaBbrVLjV52lMvgQg5we5qpMfiwzyvZ16xDy6I88hxuddq+mawtPsbqTS40to5Hd7l/aX6oG1DnPka0b/NzHsMjug4UH/FGHQcNq1hNEihJQ2HXdksMcH0FBLL6xJ5fhyxr36gJt41t3IYLkD+LzPvo16FiVVnYAkFtoY+eK93nRVtPdtNlsMckBsCt+ysY9NtRHEANowAKzyn7IxOSqi7lR3YD4mpXNIF25cbmPJJqUvQB4rL6kneLT9qHG9gp+FfalXD+ka5cLulxrDYxCPjIyasTIskMiOMqyEEHzBFSpUfS4/BPadI65COVBXHH+Ky7m6lds52H7HFfalbI8Otmirbo5xZZgzMWOfM5rZtUGwseSO1SpVSH+MlReWNVzj+Fc15tLmayuEuLZykq85B7+h94qVKA1pJ2mHOla5d3MNmZRETKpLEL7jit+47fMVKlIl08l5MVHLJL9PtSpUoBB//2Q==')
        st.caption(f'Released on : {temp.release_date.values[0]}, Rating: {temp.vote_average.values[0]}')
        print()
        st.caption(temp['overview'].values[0])
        print()
        print()
        print()
        
        num_made_recommends+=1

    



    
    



    
    
    
