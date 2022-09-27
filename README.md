# Recommendation System

Content-based Recommendation System that recommends closest movies based on similarity in content (movie plot) with the movie name provided.
Uses Nearest-Neighbors algorithm. Further filtering done based on movie language and rating.


```
git clone https://github.com/ayanatherate/World-Movies-RecommendationSys_and_Visualization.git
cd World-Movies-RecommendationSys_and_Visualization
pip install -r requirements.txt
streamlit run movies_recommender_app.py

```







# World-Movies-Visualization
Deep-dive NLP: Visual exploration and analysis of movie scripts of top movie-producing languages across the world.

Used:
1) WordCloud Visualization and Topic Modelling/pyLDAvis of movie plots of top 50 movies (by popularity) from top countries
2) Cosine Similarity (used BERT Embeddings) comparison between movie plots of countries.
3) Visualization of movie plots in 2D, separated by different timeframes


