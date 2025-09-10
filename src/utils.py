import json
import os

STATE_FILE = "data/story.json"

def load_story():
    if os.path.exists(STATE_FILE):
        with open(STATE_FILE, "r") as f:
            return json.load(f)
    return {"inventory": [], "quests": [], "npcs": {}}

def save_story(story):
    os.makedirs("data", exist_ok=True)
    with open(STATE_FILE, "w") as f:
        json.dump(story, f, indent=2)
