# Script to generate persona using scraped data and LLM
from transformers import pipeline
import json
import os

# Load GPT-2 model
generator = pipeline("text-generation", model="gpt2")

def load_user_data(filename):
    with open(filename, "r", encoding="utf-8") as f:
        return json.load(f)

def generate_persona(data):
    combined_text = "\n\n".join(data["posts"] + data["comments"])
    prompt = (
        f"Based on the following Reddit posts and comments, generate a detailed user persona including:\n"
        f"- Personality traits\n- Interests\n- Communication style\n- Possible background\n\n"
        f"Also cite a specific post or comment that supports each trait.\n\n"
        f"{combined_text}"
    )
    result = generator(prompt, max_length=1024, do_sample=True, temperature=0.7)
    return result[0]['generated_text']

def save_persona(username, persona_text):
    os.makedirs("output", exist_ok=True)
    output_file = f"output/{username}_persona.txt"
    with open(output_file, "w", encoding="utf-8") as f:
        f.write(persona_text)
    print(f"✅ Persona saved to {output_file}")

if __name__ == "__main__":
    username = input("Enter Reddit username (to generate persona): ").strip()
    data = load_user_data(f"{username}_data.json")
    persona = generate_persona(data)
    save_persona(username, persona)

