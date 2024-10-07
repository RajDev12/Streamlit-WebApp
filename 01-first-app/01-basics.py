import streamlit as st
import numpy as np
import time

st.page_link("01-basics.py", label="Home")
# st.page_link(r'P:/Course_Content/Streamlit/Feedback/Feedback.py', label="Feedback")

# https://docs.streamlit.io/develop/quick-reference/cheat-sheet

#adding title to our page
st.title("This is a Title of my APP")

st.write("This is a Normal statement")

rating = st.slider("Pick a number:",0,10,7)   #7is default value when refreshed
st.write(f"You selected : {rating}")



#creating buttons

if st.button("Click to wish"):
    # print("Happy Birthday")
    st.write("Happy Day")

#anchor link
url="https://docs.streamlit.io/develop/quick-reference/cheat-sheet"
st.link_button("Streamlit Cheatsheet",url )


#download button
st.download_button("Click to download", url)

st.feedback("thumbs")

#Adding a radio button

st.radio("Choose:", ["A","B","C"])
st.sidebar.selectbox("Pick one:", ["cats", "dogs"])


st.sidebar.button("Submit")
st.sidebar.text_input("Enter Phone NO:")

with st.chat_message("user"):
    st.write("Hello 👋")
    st.line_chart(np.random.randn(30, 3))
    
# st.chat_input("Say something")
with st.container():
    st.chat_input("Say something")


# with st.spinner(text="In progress"):
#     time.sleep(0)
#     st.success("Done")
#     st.snow()


st.sidebar.file_uploader("Upload a CSV")


# st.experimental_audio_input("Record a voice message")
# st.camera_input("Take a picture")
# st.color_picker("Pick a color")