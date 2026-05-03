import streamlit as st
from job_recommender import recommend_jobs

st.title("Job Recommendation System")
st.write("Enter your skills separated by spaces")
skills=st.text_input("Example: python sql machine learning")
if st.button("Recommend Jobs"):
    if skills:
        results=recommend_jobs(skills)
        st.subheader("Recommended Job IDs:")
        
        for job in results:
            st.write(job)

    else:
        st.warning("Please enter skills first")