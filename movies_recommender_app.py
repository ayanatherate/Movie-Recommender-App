

import pandas as pd
import numpy as np
import streamlit as st
import time
import re


st.set_page_config(page_title='Movie Recommendation App', page_icon=None, layout="centered", initial_sidebar_state="auto", menu_items=None)
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
    if len(inp)>1:
        num_movies=st.select_slider('Select number of recommendations you want',options=[1,2,3,4,5,6,7,8,9,10])
    inp=inp.lower()
    inp=re.sub('[^a-zA-Z0-9 ]','',inp)
    return inp



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

inp=take_inp()
if inp=='':
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

while num_made_recommends<num_movies:
    for i in recommendation:
        temp= data[data['id']==i]
        st.write('----------------------')
        time.sleep(1)
        st.write(temp['title'].values[0])
        st.caption(f'Released on : {temp.release_date.values[0]}, Rating: {temp.vote_average.values[0]}')
        print()
        st.caption(temp['overview'].values[0])
        print()
        print()
        print()
        
        num_made_recommends+=1

    



    
    



    
    
    
