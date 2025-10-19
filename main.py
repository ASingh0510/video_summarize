from video_utils import load_mp4, download_yt_vid, convert_to_wav
from summarize import summarize_text
import os
import sys
import glob
import whisper

DATA_DIR = "data"

def main():
    if len(sys.argv) <= 1:
        print("Usage: python main.py <file_path_or_youtube_link>")
        return

    print("Working atm...")

    input_arg = sys.argv[1]

    # Handle YouTube or local file input
    if input_arg.startswith('https'):
        print("Detected YouTube link.")
        download_yt_vid(input_arg)
    elif input_arg.endswith(('.mp4', '.mp3')):
        print("Detected local media file.")
        load_mp4(input_arg)
    else:
        print("Invalid input. Please provide a YouTube link or media file.")
        return

    # Find the latest media file in data/
    media_files = glob.glob(os.path.join(DATA_DIR, "*.mp4")) + glob.glob(os.path.join(DATA_DIR, "*.mp3"))
    if not media_files:
        print(f"No media files found in {DATA_DIR}!")
        return

    latest_media = max(media_files, key=os.path.getmtime)

    # Convert media to WAV
    wav_file = convert_to_wav(latest_media)
    if not wav_file:
        print("Failed to convert to WAV.")
        return

    # Transcribe audio with Whisper
    print("Transcribing audio using Whisper (base model)...")
    model = whisper.load_model("base")
    result = model.transcribe(wav_file)

    print("\n--- Transcription ---\n")
    print(result["text"])

    # Save transcription to file
    base_name = os.path.splitext(os.path.basename(wav_file))[0]
    txt_path = os.path.join(DATA_DIR, f"{base_name}.txt")

    with open(txt_path, "w", encoding="utf-8") as f:
        f.write(result["text"])

    print(f"\nTranscription saved to {txt_path}")

    # Summarize 
    print("\nGenerating summary...")
    summarize_text(txt_path)


if __name__ == "__main__":
    main()
