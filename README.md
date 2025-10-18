# Video Summarizer

A simple Python project that downloads YouTube videos, extracts audio, and generates a summary using OpenAI Whisper and text summarization.

## Features
- Download videos from YouTube
- Convert MP4/MP3 → WAV automatically
- Transcribe and summarize video content

## Setup

# bash
git clone https://github.com/ASingh0510/video_summarize.git

cd video_summarize

pip install -r requirements.txt

python main.py

Then download FFMPEG using:
# macOS
brew install ffmpeg

# Ubuntu/Debian
sudo apt install ffmpeg

# Windows
choco install ffmpeg

## Virtual Environment Setup

It’s recommended to use a **virtual environment** so that your project dependencies don’t interfere with system-wide packages.

# 1. Create a virtual environment

python -m venv whisper-env

# 2. Activate the environment
Windows : whisper-env\Scripts\activate 
Mac/Linux: source whisper-env/bin/activate
Arch/Fish: source whisper-env/bin/activate.fish


# Since the tool works with chatgpt you will need an api key which is easy to make and free to use.

1. https://platform.openai.com/api-keys
2. Make an api key but never share it with anyone.
3. Set it up while being in the whisper env.
# macOS/Linux
export OPENAI_API_KEY="your_api_key_here"
# Arch
set -x set -x OPENAI_API_KEY "your_api_key_here"
# Windows (PowerShell)
setx OPENAI_API_KEY "your_api_key_here"


## Usage
# From YouTube
python main.py "https://www.youtube.com/watch?v=dQw4w9WgXcQ"

# From a local file
python main.py "path/to/video.mp4"

