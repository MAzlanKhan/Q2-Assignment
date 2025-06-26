from dotenv import load_dotenv
import os

class Secrets:
    def __init__(self):
        self.gemini_api_key = os.getenv("GEMINI_API_KEY")
        self.gemini_api_model = os.getenv("GEMINI_API_MODEL")
        self.base_url = os.getenv("BASE_URL")