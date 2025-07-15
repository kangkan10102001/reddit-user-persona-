import requests
from bs4 import BeautifulSoup
import json
import time

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
}

def get_reddit_comments(username, limit=50):
    url = f"https://www.reddit.com/user/{username}/comments/"
    comments = []

    try:
        response = requests.get(url, headers=headers)
        soup = BeautifulSoup(response.content, "html.parser")
        comment_tags = soup.find_all("div", class_="Comment")

        for tag in comment_tags[:limit]:
            text_tag = tag.find("p")
            if text_tag:
                comments.append(text_tag.text.strip())

    except Exception as e:
        print(f"Error fetching comments: {e}")

    return comments

def get_reddit_posts(username, limit=20):
    url = f"https://www.reddit.com/user/{username}/posts/"
    posts = []

    try:
        response = requests.get(url, headers=headers)
        soup = BeautifulSoup(response.content, "html.parser")
        post_tags = soup.find_all("div", class_="Post")

        for tag in post_tags[:limit]:
            title_tag = tag.find("h3")
            if title_tag:
                posts.append(title_tag.text.strip())

    except Exception as e:
        print(f"Error fetching posts: {e}")

    return posts

def save_user_data(username):
    print(f"Fetching data for Reddit user: {username}")
    posts = get_reddit_posts(username)
    time.sleep(2)  # Pause to avoid blocking
    comments = get_reddit_comments(username)

    data = {
        "username": username,
        "posts": posts,
        "comments": comments
    }

    with open(f"{username}_data.json", "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4)

    print(f"✅ Data saved to {username}_data.json")

if __name__ == "__main__":
    username = input("Enter Reddit username: ").strip()
    save_user_data(username)

