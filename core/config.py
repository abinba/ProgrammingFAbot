import os
from dotenv import load_dotenv

ENV_PATH = os.path.dirname(os.path.dirname(__file__))

load_dotenv()

TELEGRAM_BOT_TOKEN = os.environ.get("TELEGRAM_BOT_TOKEN")
OPENAI_API_KEY = os.environ.get("OPENAI_API_KEY")
