import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from datetime import timedelta


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

    # Accept an uploaded CSV file in the sidebar
    uploaded_file = st.sidebar.file_uploader("Upload a CSV file.", type="csv")

    #plot the data
    if uploaded_file is not None:
        data = pd.read_csv(uploaded_file)
        data['Date'] = pd.to_datetime(data['Date'])
        data = data.sort_values('Date')

        # Add a title to the bar chart
        st.subheader("Active portfolio project ideas over time")

        # Plot the 'Project Ideas' column as a bar chart
        plt.bar(data['Date'], data['Project Ideas'])

        # Plot the 'Conversations' column as a thin red vertical line
        for date in data[data['Conversations'] > 0]['Date']:
            plt.axvline(x=date + timedelta(hours=10), color='red', linewidth=0.5)

        # Rotate the dates 45 degrees
        plt.xticks(rotation=45)

        # Display the plot
        st.pyplot(plt.gcf())

if __name__ == "__main__":
    main()