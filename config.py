import json
import os

def load_config():
  with open('./secrets.json', 'r') as f:
    secrets = json.load(f)
  os.environ["DISCORD_API_KEY"] = secrets["DISCORD_API_KEY"]
  os.environ["OPENAI_API_KEY"] = secrets["OPENAI_API_KEY"]
