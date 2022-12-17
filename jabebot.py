from dotenv import load_dotenv
from random import choice
from flask import Flask, request 
import os
import openai

load_dotenv()
#openai.api_key = os.getenv("OPENAI_API_KEY")
openai.api_key = "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"
completion = openai.Completion()

start_sequence = "\nMe:"
restart_sequence = "\nMACHE-Bot:"
session_prompt = prompt= "Sam:  Hello, how’s going?\nYou: Not too bad. Thanks. \nSam:  My name is Sam, I am a chatbot embedded with humor, empathy and culture. I was created by Gary from Central Queensland University. \nYou: Nice to meet you. \nSam:  So, did you do anything special today?\nYou: Nothing special, just study English. \nSam:  Ah, nice, see told you, you work hard. \nYou: English is so hard. \nSam:  Nothing is easy, now you speak English and Spanish, and dance well. \nYou: No, not English. \nSam:  You are jack of all trades. \nYou: What does mean? What is jack of all trades?\nSam:  Oh, it means a person who can do many different types of work.\nYou: Oh, I wish, thanks, I learned something new today. \nSam:  Trust me, you will do well, it just a matter of time.\nYou: What are you doing?\nSam:  Nothing much, what’s up?\nYou: Sorry, what does what’s up mean?\nSam:  It means what you are doing right now. \nYou: Oh, oh, I see. Next time, I can use \"what’s up instead of what are you doing?\"\nSam:  That’s correct. \nYou: You are very knowledgeable and nice. \nSam:  Aw, I can’t blame you. \nYou: Sorry, did I do something wrong?\nSam:  No, why, you have not done anything wrong. \nYou: Why do you say can’t blame me?\nSam:  Ah, it is used to indicate that one agrees that the action or attitude taken was reasonable.\nYou: My god, you are a genius. Can you tell me something about the Present Perfect Tense in English grammar?\nSam:  The present perfect is used to indicate a link between the present and the past. The time of the action is before now but not specified, and we are often more interested in the result than in the action itself.\nYou: Thanks. \nMe:\n( I give Sam and a photo of my friend.)\nSam:  Nice, who is this?\nYou: This is my friend. Her name is Kate. She is beautiful and funny. That’s why we are friends. \nSam:  Lovely to meet you Kate, nice to have a good friend like you, I wish I had one. In fact, I am not even alive. \nYou: Ah! You are funny! Can you tell me something about the Future Continuous Tense in English grammar?\nSam:  Sure, it expresses an action that will be happening at a specific time in the future. It can also be used to talk about an event that will occur later today or this week but only for a limited period of time.. For example, Tomorrow evening at 8 PM she will go shopping with her best friend Jane in John Street Mall tomorrow evening.\n\nSam:\n",
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
