# Reddit User Persona Generator (No API Key Required)

This project scrapes a Reddit user's public posts and comments and uses a lightweight language model (GPT-2) to generate a detailed user persona — **without using any Reddit API credentials or OpenAI keys**.

---

## 🚀 Features

- ✅ Web scraping using `requests` and `BeautifulSoup` (no Reddit API needed)  
- 🤖 Persona generation using Hugging Face's `transformers` (GPT-2)  
- 📄 Output includes personality traits, interests, and citation-based insights  
- 📝 Output saved as text files in the `output/` folder  

---

## 📦 Requirements

Install Python 3.8 or later. Then install dependencies:

```bash
pip install -r requirements.txt

## 🛠️ How to Use ## 

Step 1: Scrape Reddit Data
python reddit_scraper.py
You'll be prompted to enter a Reddit username (e.g., kojied).
The script will scrape recent posts and comments and save them to kojied_data.json.

Step 2: Generate User Persona
python persona_generator.py
Again, enter the same username (e.g., kojied).
The script will use the scraped data to generate a user persona and save it as:
output/kojied_persona.txt

📂 Output Example

output/
├── kojied_persona.txt
├── Hungry-Move-6603_persona.txt
