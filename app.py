# Import Streamlit for creating web apps, and dotenv for loading environment variables.
import streamlit as st
from dotenv import load_dotenv

# Load environment variables from a .env file.
load_dotenv()

# Import the os module for accessing environment variables.
import os

# Import Google's generative AI library to use its summarization model.
import google.generativeai as genai

# Import YouTubeTranscriptApi to fetch transcripts from YouTube videos.
from youtube_transcript_api import YouTubeTranscriptApi

# Configure the Google API by setting the API key from environment variables.
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# Prompt string for the summarization task.
prompt = """You are a YouTube video summarizer. You will take the transcript text,
and summarize the entire video into key points within 300 words. Please provide the summary of the text given here: """

# Define a function to extract and concatenate transcript text from a YouTube video URL.
def extract_transcript_details(youtube_video_url):
    try:
        # Extract the video ID from the URL.
        video_id = youtube_video_url.split("=")[1]
        
        # Fetch the transcript using the YouTubeTranscriptApi.
        transcript_text = YouTubeTranscriptApi.get_transcript(video_id)

        # Concatenate the text from the transcript into a single string.
        transcript = ""
        for i in transcript_text:
            transcript += " " + i["text"]

        return transcript

    except Exception as e:
        # Raise any exceptions that occur during the process.
        raise e
    
# Define a function to generate a summary using the Gemini Pro model from Google.
def generate_gemini_content(transcript_text, prompt):
    # Initialize the Gemini Pro model.
    model = genai.GenerativeModel("gemini-pro")

    # Generate the content summary by passing the prompt and transcript.
    response = model.generate_content(prompt + transcript_text)
    return response.text

# Set the title of the Streamlit web app.
st.title("BreviTube: Quick Summaries for YouTube Videos")

# Create an input field for the user to enter the YouTube video link.
youtube_link = st.text_input("Enter YouTube Video Link:")

# Display the video thumbnail if a link is provided.
if youtube_link:
    video_id = youtube_link.split("=")[1]
    st.image(f"http://img.youtube.com/vi/{video_id}/0.jpg", use_column_width=True)

# Button to trigger the transcription and summarization process.
if st.button("Get Detailed Notes"):
    # Extract the transcript text from the provided YouTube link.
    transcript_text = extract_transcript_details(youtube_link)

    # Generate the summary if transcript text is available.
    if transcript_text:
        summary = generate_gemini_content(transcript_text, prompt)
        st.markdown("## Detailed Notes:")
        st.write(summary)