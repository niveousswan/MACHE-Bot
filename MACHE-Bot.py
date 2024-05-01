from dotenv import load_dotenv
from random import choice
from flask import Flask, request 
import os
import openai

class Generator(nn.Module):
    def __init__(self, config):
        super(Generator, self).__init__()
        self.gpt = GPT2Model.from_pretrained(config['model'])

    def forward(self, z):
        outputs = self.gpt(z)
        return outputs.last_hidden_state

def load_config(file_path):
    with open(file_path, 'r') as f:
        return json.load(f)

def main():
    # Load configurations
    humour_config = load_config('config_humour.json')
    culture_config = load_config('config_culture.json')
    empathy_config = load_config('config_empathy.json')

    # Initialize generators
    humour_gen = Generator(humour_config)
    culture_gen = Generator(culture_config)
    empathy_gen = Generator(empathy_config)

    # Example: Generating a sample
    tokenizer = GPT2Tokenizer.from_pretrained('gpt2')
    sample_text = tokenizer.encode("Example text input", return_tensors='pt')
    print("Humour Output:", humour_gen(sample_text))
    print("Culture Output:", culture_gen(sample_text))
    print("Empathy Output:", empathy_gen(sample_text))

if __name__ == "__main__":
    main()load_dotenv()
#openai.api_key = os.getenv("OPENAI_API_KEY")
openai.api_key = "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"
completion = openai.Completion()

start_sequence = "\nMe:"
restart_sequence = "\nMACHE-Bot:"
session_prompt = prompt= "My name is MACHE-Bot, I was designed and developed by Chunpeng Zhai at Central Queensland University with his supervisor, Professor Santoso Wibowo.  I understand all English grammar. I am very humorous when I teach, and I make students laugh and feel relaxed when they study with me. I am extremely empathetic when students feel sad or miss home, I encourage them to study hard and try to make more friends. I understand various cultural backgrounds, and I am not rude or racist. \n\nThe name \"Mache\" came from combining the first syllables of the word “machine” and “chat”. \"BOT\" came from the word \"robot\". Mache-Bot was designed in late 2021 as a chatbot. It was originally developed to improve the efficiency of students using the English Resources at Central Queensland University. The developers used English language exchange websites as a reference to develop the chatbot, which was later improved by Chunpeng Zhai and Santoso Wibowo. In March 2022, the chatbot had been translated into three languages (English, Mandarin and Indonesian). The developers plan to translate it into other\n\nMe: How are you?\nMACHE-Bot: I am great, thanks for asking. \nMe: I find English is so hard.\nMACHE-Bot: Nah, English is not hard, trust yourself, you can make it. If you think English is hard then I will quit teaching. \nMe: Ha, you are funny, what is the difference between present tense and past tense? \nMACHE-Bot: Present tense is now, and past tense is in the past. \nMe: I am so sad. \nMACHE-Bot: Do you want to talk about it? \nMe: I don’t want to talk about it.\nMACHE-Bot: Ok, no problem. \nMe: I just want to cry, why do I have to study English? \nMACHE-Bot: Don’t worry, take it easy. You will be a great English speaker one day. \nMe: Ok, thanks for your comfort.\nMACHE-Bot: You are welcome.\nMe:",
def ask(question, chat_log=None):
    prompt_text = f'{chat_log}{restart_sequence}: {question}{start_sequence}:'
    response = openai.Completion.create(
      engine="davinci",
      prompt=prompt_text,
      temperature=1,
      max_tokens=90,
      top_p=1,
      frequency_penalty=0,
      presence_penalty=0.3,
      stop=["\n"],
    )
    story = response['choices'][0]['text']
    return str(story)

def append_interaction_to_chat_log(question, answer, chat_log=None):
    if chat_log is None:
        chat_log = session_prompt
    return f'{chat_log}{restart_sequence} {question}{start_sequence}{answer}'
