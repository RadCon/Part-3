import markovify
import random
import config
from mlh_twitter_api import get_user_tweets as fetch
from twitter_scraper_fetcher import *
import re
    
 
# build the markov chain based on the text we read
# we use the markovify library to do this step
def generate_bot_answer(twitter_handle, user_question):
    tweets = fetch(twitter_handle)  
    clean_tweets = clean_tweets_data(tweets)   
    text = ''.join(map(str, clean_tweets)) 
    text_model = markovify.Text(text)   
    return generate_bot_answer_with_text_model(twitter_handle, user_question, text_model)
    
def generate_bot_answer_with_text_model(twitter_handle, user_question, text_model):
    bot_answer = None
    
    word_list = user_question.split(' ') 
    random_word = random.choice(word_list) 
    bot_answer = text_model.make_sentence_with_start(random_word, strict=False) 
    
    if bot_answer == None:  
      bot_answer = text_model.make_sentence(test_output=False)  
    return bot_answer

    
    