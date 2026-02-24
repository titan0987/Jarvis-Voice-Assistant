# Jarvis - Python Voice Assistant

A voice-controlled assistant built using Python that can perform web automation, play music, fetch news, and respond using AI.

## Features

- Voice recognition using SpeechRecognition
- Text-to-speech using pyttsx3
- Open websites (Google, YouTube, LinkedIn, etc.)
- Play YouTube music
- Play local downloaded songs
- Fetch top news headlines
- AI-based short responses using Gemini API
- Pause, resume, and stop music playback

## Technologies Used

- Python
- SpeechRecognition
- pyttsx3
- Requests
- VLC
- Google Generative AI API

## Installation

1. Clone the repository:

   git clone https://github.com/yourusername/Jarvis-Voice-Assistant.git

2. Install dependencies:

   pip install -r requirements.txt

3. Set environment variables:

   GEMINI_API_KEY = your_api_key
   NEWS_API_KEY = your_news_api_key

4. Run the project:

   python main.py

## Notes

- use python 3.11.0 version
- PyAudio installation may require wheel installation on Windows.
- Ensure microphone access is enabled.