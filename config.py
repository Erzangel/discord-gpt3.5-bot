import json
import os

def load_config():
  with open('./secrets.json', 'r') as f:
    secrets = json.load(f)
  os.environ["DISCORD_API_KEY"] = secrets["AZURE_URI_GPT35TURBO"]
  os.environ["OPENAI_API_KEY"] = secrets["AZURE_API_KEY"]
