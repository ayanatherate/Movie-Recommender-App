# -*- coding: utf-8 -*-
"""
@author: Ayan
"""

import pandas as pd
import numpy as np
import streamlit as st
import time

st.title('Movies Recommender')
st.subheader('Let AI decide for you, what to watch next!')

def take_inp():
    inp=st.text_input(label='Enter a movie name, you just watched:')
    return inp



data=pd.read_csv(r'C:\Users\User\World-Movies-RecommendationSystem_and_Visualization\Recommendation_Database\Recommendations_data.csv')

#print(data['recommendaions'])

match_names=[data['normalized_names'][i] for i in range(len(data))]

def map_names(name):
    movie_index=''
    
    for i in range(len(match_names)):
        if name==match_names[i]:
            movie_index=i
            
    return movie_index

inp=take_inp()
if inp=='':
    st.stop()
else:
    movie_index_=map_names(inp)

recommendation=[]

for i in data['recommendaions'][movie_index_].split(','):
    recommendation.append(int(i))
st.caption('Here are your recommended movie lists:')   
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


    
    



    
    
    
