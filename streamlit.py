import streamlit as st

def main():
    # Header
    st.title("This is a title!")
    
    # Subtitle
    st.subheader("This is a subheader.")
    
    # Text
    st.write("This is text.")
    
    # Video
    st.subheader("This is a very important video.")
    video_url = "https://www.youtube.com/watch?v=y8Kyi0WNg40"
    st.video(video_url)

if __name__ == "__main__":
    main()