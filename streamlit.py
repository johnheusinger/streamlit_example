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

    #Sidebar
    st.sidebar.write("This is a sidebar.")

    #Add two images to the sidebar, with a radio button to switch between them

    image1 = "happy.jpg"
    image2 = "sad.jpg"
    image_choice = st.sidebar.radio("Choose an image.", [image1, image2])

    st.sidebar.image(image_choice)

if __name__ == "__main__":
    main()