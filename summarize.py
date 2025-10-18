import os
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
