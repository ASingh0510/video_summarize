import yt_dlp # This is library which helps to download youtube videos.
import os # Helps moving files and stuff.
import subprocess 
import whisper


DATA_DIR = "data"
os.makedirs(DATA_DIR, exist_ok=True)

COOKIES_PATH = os.path.expanduser("~/cookies.txt")

def download_yt_vid(url):
    ydl_opts = {
        'outtmpl': os.path.join(DATA_DIR, '%(title)s.%(ext)s'),  # Save in data/ folder
        'format': 'bestvideo+bestaudio/best',                    # Pick best video and audio
        'merge_output_format': 'mp4',                            # Force output to MP4
        'noplaylist': True                                       # Ignore playlists can be set to false if u want to
    }

    if os.path.exists(COOKIES_PATH):
        ydl_opts['cookiefile'] = COOKIES_PATH
        print(f"Using cookies from: {COOKIES_PATH}")

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])

def load_mp4(file_path):
    if os.path.exists(file_path) and (file_path.endswith(".mp4") or file_path.endswith(".mp3")):   
        print(f"Your file has been found at {file_path}")           
        dest = os.path.join(DATA_DIR, os.path.basename(file_path))    
        import shutil
        shutil.copy(file_path, dest)
        print(f"Copied to {dest}")
    else:
        print("File not found or not an valid path!")

def convert_to_wav(video_path):
    if not os.path.exists(video_path): 
        print("Video not found.")
        return None

    Original = os.path.splitext(os.path.basename(video_path))[0] 
    # basename gets the video path name and splittext removes .mp4/.mp3 from the end
    wav_path = os.path.join("data", f"{Original}.wav")
    # this changes the file type from .mp4/.mp3 to .wav

    # run ffmpeg command to extract audio
    command = [
        "ffmpeg",
        "-i", video_path,    # input video
        "-vn",               # no video
        "-acodec", "pcm_s16le", # WAV format
        "-ar", "44100",      # sample rate
        "-ac", "2",          # stereo
        wav_path
    ]

    print(f"Converting {video_path} → {wav_path} ...")
    subprocess.run(command, check=True)
    print("Conversion done!")

    return wav_path
    
    