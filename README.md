
https://github.com/trishcho/BreviTube/issues/1#issue-2462074397

## Authors

- [@Trishul](https://www.github.com/trishcho)


# BreviTube: Quick Summaries for YouTube Videos

BreviTube is a Streamlit-based web application that generates concise summaries of YouTube videos by extracting their transcripts and using Google's generative AI for summarization. This tool is perfect for anyone who wants to quickly grasp the key points of lengthy YouTube content.


## Features



- YouTube Transcript Extraction: Automatically extracts the transcript from any YouTube video.
- AI-Powered Summarization: Summarizes the extracted transcript into key points using Google's advanced AI models.
- Streamlit Interface: User-friendly web interface built with Streamlit.

## Setup

Clone the repository:

```bash
git clone https://github.com/yourusername/BreviTube.git
cd BreviTube
```

Create a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`

```

Install the required packages:

```bash
pip install -r requirements.txt

```

Set up environment variables:

Create a .env file in the root of your project and add your Google API key:

```bash
GOOGLE_API_KEY=your_google_api_key_here


```

Run the application:
```bash
streamlit run app.py


```
