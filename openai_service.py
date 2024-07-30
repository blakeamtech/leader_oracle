from openai import OpenAI
from typing import List, Dict
from dotenv import load_dotenv
import os

load_dotenv()

class OpenAIService:
    def __init__(self):
        self.client = OpenAI(api_key=os.getenv('OPENAI_KEY'))

    def generate_response(self, conversation_history: List[Dict[str, str]]) -> str:
        if not isinstance(conversation_history, list):
            raise ValueError("Conversation history must be a list of message dictionaries.")
        
        try:
            response = self.client.chat.completions.create(model="gpt-4o-mini", messages=conversation_history)
            return response.choices[0].message.content
        except Exception as e:
            print(f"Error generating response: {e}")
            return ""

# Usage example:
# openai_service = OpenAIService()
# embedding = openai_service.get_text_embedding("Example text")
# response = openai_service.generate_response([{"role": "user", "content": "Hello!"}])