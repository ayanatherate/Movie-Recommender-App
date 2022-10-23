

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

if inp=='' and num_movies<0:
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
        st.image('data:image/jpeg;base64,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')
        st.caption(f'Released on : {temp.release_date.values[0]}, Rating: {temp.vote_average.values[0]}')
        print()
        st.caption(temp['overview'].values[0])
        print()
        print()
        print()
        
        num_made_recommends+=1

    



    
    



    
    
    
