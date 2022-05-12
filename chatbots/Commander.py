from transformers import pipeline
from chatbots.Chatbot import Chatbot

class Commander(Chatbot):
    def __init__(self):
        super().__init__()
        self.generator = pipeline('text-generation', model='Dizzykong/gpt2-large-quests', tokenizer='gpt2')


    def send_message(self):
        result = self.generator(f"\n{self.response['text']}\t", max_length=200, num_return_sequences=1)[0]
        result = result['generated_text']
        result = result.split('\n')[1]
        return {"text": result}

    def recv_message(self, message):
        self.response = message
        return super().recv_message(message)