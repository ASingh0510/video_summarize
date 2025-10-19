from transformers import pipeline
import os

# device=-1 uses CPU by default
# if you want to use GPU, change device=-1 to device=0
summarizer = pipeline("summarization", model="facebook/bart-large-cnn", device=-1)

def summarize_text(file_path):
    with open(file_path, "r", encoding="utf-8") as f:
        text = f.read()

    # Split into chunks for long texts
    max_chunk_size = 1000
    chunks = []
    while len(text) > max_chunk_size:
        split_at = text.rfind(" ", 0, max_chunk_size)
        chunks.append(text[:split_at])
        text = text[split_at:]
    chunks.append(text)

    # Summarize chunks
    summaries = [summarizer(c, max_length=150, min_length=40, do_sample=False)[0]['summary_text'] for c in chunks]
    final_summary = " ".join(summaries)

    summary_file = os.path.join("data", os.path.splitext(os.path.basename(file_path))[0] + "_summary_offline.txt")
    with open(summary_file, "w", encoding="utf-8") as f:
        f.write(final_summary)

    print(f"\nOffline summary saved to {summary_file}\n")
    print(final_summary)
    return summary_file



# The below code was the previous summarizer which ran on openai api key its better but i am not very sure if its free or not, I used it for my usage was 0$ even with a lot 
# of testing so maybe i was on trail please look into it if you wanna use it, the code runs well and summaries are better if you use this code.

""" import os
from openai import OpenAI

client = OpenAI()

def summarize_text(file_path):
    with open(file_path, "r", encoding="utf-8") as f:
        text = f.read()

    base_name = os.path.splitext(os.path.basename(file_path))[0]
    summary_file = os.path.join("data", f"{base_name}_summary.txt")

    print("Summarizing with ChatGPT...")

    prompt = f"Summarize the following text in clear, structured English:\n\n{text}"

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "You are an expert summarizer."},
            {"role": "user", "content": prompt}
        ]
    )

    summary_text = response.choices[0].message.content.strip()

    with open(summary_file, "w", encoding="utf-8") as f:
        f.write(summary_text)

    print(f"\nSummary saved to {summary_file}")
    print("\n--- Summary ---\n")
    print(summary_text)
    return summary_file
"""