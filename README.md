BreviTube: Quick Summaries for YouTube Videos
BreviTube is a Streamlit-based web application that generates concise summaries of YouTube videos by extracting their transcripts and using Google's generative AI for summarization. This tool is perfect for anyone who wants to quickly grasp the key points of lengthy YouTube content.

Features
YouTube Transcript Extraction: Automatically extracts the transcript from any YouTube video.
AI-Powered Summarization: Summarizes the extracted transcript into key points using Google's advanced AI models.
Streamlit Interface: User-friendly web interface built with Streamlit.
Installation
Prerequisites
Python 3.7 or higher
A Google Cloud API Key with access to the generative AI services
Streamlit
dotenv
youtube-transcript-api
Setup
Clone the repository:

bash
Copy code
git clone https://github.com/yourusername/BreviTube.git
cd BreviTube
Create a virtual environment:

bash
Copy code
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
Install the required packages:

bash
Copy code
pip install -r requirements.txt
Set up environment variables:

Create a .env file in the root of your project and add your Google API key:

makefile
Copy code
GOOGLE_API_KEY=your_google_api_key_here
Run the application:

bash
Copy code
streamlit run app.py
Usage
Enter the YouTube video link:
Paste the URL of the YouTube video you want to summarize into the input field.

Get Detailed Notes:
Click on the "Get Detailed Notes" button. The application will fetch the transcript, summarize it, and display the key points.

Project Structure
app.py: The main application file that runs the Streamlit web app.
.env: Environment variables file to securely store your API keys.
requirements.txt: A list of Python dependencies required for the project.
How It Works
Transcript Extraction:
The application uses the YouTubeTranscriptApi to fetch the transcript of the video based on the provided YouTube link.

Summarization:
The extracted transcript is passed to the Gemini Pro model of Google's generative AI library, which then generates a concise summary.

User Interface:
The Streamlit interface allows users to input YouTube video links and displays the corresponding video thumbnail along with the generated summary.

Contributing
Contributions are welcome! Please fork this repository, make your changes, and submit a pull request.

License
This project is licensed under the MIT License - see the LICENSE file for details.

Acknowledgements
Streamlit for providing an easy way to create web apps in Python.
Google Generative AI for powering the summarization.
YouTubeTranscriptApi for extracting YouTube video transcripts.
