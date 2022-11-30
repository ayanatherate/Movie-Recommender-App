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
        try:
            imgurl=thumb['src']
            imgurl='https://themoviedb.org/'+imgurl
        
            st.image(imgurl)
        except:
            st.image('data:image/gif;base64,R0lGODlhAQABAIAAAP///////yH5BAEKAAEALAAAAAABAAEAAAICTAEAOw==')
            #st.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')
        
        #st.image+AGb32huPHb/Rqp9MNlepMh9knnP96o3cjxsdykMvDKfz5VXll8wpeWVAQWgy0OVptOj3n20JRs+nH9MVKtW8SxR7VXGSTxX2sVlHO4iWUDIBKnK5qjc6Pp1zO01xYwSSuu1nZASR8a0c18dlRGZvqqM5od/DaDSWVjZ3bxWsEUCDA2ouM1ptphNgyqAJgxdD/aq+iwi5vJbphkFs5NaOt30mn2El3FD4qxDc6g87fMj89s0dtPXReOPtL/AEpWMi31iCvJA2stcBBcxZWFQVzkb/KsPS9VNuwvIjuif94oGPnii2012zniDRtG3xPIrcmSpQbRQhs3kl3zjLfyjtXTUrlLOHZuG48sfSvOrdSWNlEWeVQfIDuaBbrVLjV52lMvgQg5we5qpMfiwzyvZ16xDy6I88hxuddq+mawtPsbqTS40to5Hd7l/aX6oG1DnPka0b/NzHsMjug4UH/FGHQcNq1hNEihJQ2HXdksMcH0FBLL6xJ5fhyxr36gJt41t3IYLkD+LzPvo16FiVVnYAkFtoY+eK93nRVtPdtNlsMckBsCt+ysY9NtRHEANowAKzyn7IxOSqi7lR3YD4mpXNIF25cbmPJJqUvQB4rL6kneLT9qHG9gp+FfalXD+ka5cLulxrDYxCPjIyasTIskMiOMqyEEHzBFSpUfS4/BPadI65COVBXHH+Ky7m6lds52H7HFfalbI8Otmirbo5xZZgzMWOfM5rZtUGwseSO1SpVSH+MlReWNVzj+Fc15tLmayuEuLZykq85B7+h94qVKA1pJ2mHOla5d3MNmZRETKpLEL7jit+47fMVKlIl08l5MVHLJL9PtSpUoBB//2Q==')
        st.caption(f'Released on : {temp.release_date.values[0]}, Rating: {temp.vote_average.values[0]}')
        print()
        st.caption(temp['overview'].values[0])
        print()
        print()
        print()
        
        num_made_recommends+=1

    


    
    

    
    



    
    
    
