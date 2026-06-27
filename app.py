import streamlit as st
from crew_setup import crew

st.set_page_config(page_title="AI News Agent", page_icon="📰")

st.title("📰 AI News Agent")
st.write("Get the latest AI news from around the world.")

if st.button("Get Latest AI News"):
    with st.spinner("Searching for latest AI news..."):
        result = crew.kickoff()

    st.subheader("Latest AI News")
    st.write(result.raw)