import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity

df=pd.read_csv('job_dataset.csv')
df['User_Skills']=df['User_Skills'].str.lower()

vectorizer=CountVectorizer()
skill_matrix=vectorizer.fit_transform(df['User_Skills'])

def recommend_jobs(user_input):
    user_input=[user_input.lower()]
    user_vector=vectorizer.transform(user_input)
    similarity_scores=cosine_similarity(user_vector,skill_matrix)
    top_matches=similarity_scores.argsort()[0][-5:]
    recommended=df.iloc[top_matches]['Job_ID'].unique()
    
    return recommended

