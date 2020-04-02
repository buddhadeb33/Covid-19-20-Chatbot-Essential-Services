#import io
import random
import string # to process standard python strings
#import warnings
import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import warnings
warnings.filterwarnings('ignore')
import nltk
from nltk.tokenize import sent_tokenize
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer
from nltk.stem import PorterStemmer
raw ="""How dangerous is the coronavirus Covid-19 is deadly, although fatality rates skyrocket for the elderly and those with compromised immune systems.How has the coronavirus affected you Well if you ask me personally, the outbreak of novel Coronavirus, has affected me significantly. Both in respect of career and in respect of mental health. Is there a treatment for the Coronavirus They are experimenting with various medicines and it seems some anti-malarial drugs show promise. However, they help only a little bit, as evidenced by the mortality rate in places like Italy or Spain. They are best if administered early, before the lungs are damaged. Is there a vaccine for the coronavirus We don’t “find” vaccines. That’s the language yellow media uses, but it’s far from the truth.
We know the virus, and we know what it looks like. Now we need to produce a sufficient amount of attenuated virii. For that, we inject the virus into a foreign host, like a chicken embryo in an egg. Most viruses will die, because the host is so different from humans, that it can not work. Some will mutate to work, and those multiply.How did coronaviruses get their name The coronavirus family was discovered first in 1960s but we don’t know where they come from. They get the name given their crown-like (“corona”) shape. Following a December 2019 outbreak in China, the World Health Organization identified a new type called 2019 novel coronavirus (2019-nCoV).What are coronaviruses Coronavirus is a name for a group of viruses that target mammals, including cats, dogs, and humans. They’re well known for causing potentially fatal conditions like kidney failure, pneumonia but also mundane things like some instances of the common cold.
Does coronavirus cause death Statistically speaking, you have a 98% chance of survival, and 80% chance that you won’t need medical care at all even if you get infected, so stay positive, stay at home as much as possible, eat healthy, treat everyone as if they are infected, treat other as if you are infected. Many people get infected and get better without even knowing they had it.What can one do to prepare for the coronavirus? What should one buy or do regularly So, one thing you might do before it hits your region is to buy enough food for your freezer as well as canned goods and stock it so that, when the Virus hits, you won’t be running out into a store crowded with infected people. When it hits, stay home for work and school and strictly avoid crowded places. Stock up on real bar soap (like Ivory Gold) and wash hands frequently. Avoid sanitizers. Try to avoid clinics or EDs unless your symptoms become an issue as you don’t want to spread the disease beyond your home. Stock up on jello, G-Zero, plain decongestants like Mucinex, Bouillon or clear soups, lots of Kleenex and avoid solids and dairy products while you are symptomatic. The rest is just common sense.What should I buy to prepare for a coronavirus epidemic if I had to stay in my home for a very long time So, one thing you might do before it hits your region is to buy enough food for your freezer as well as canned goods and stock it so that, when the Virus hits, you won’t be running out into a store crowded with infected people. When it hits, stay home for work and school and strictly avoid crowded places. Stock up on real bar soap (like Ivory Gold) and wash hands frequently. Avoid sanitizers. Try to avoid clinics or EDs unless your symptoms become an issue as you don’t want to spread the disease beyond your home. Stock up on jello, G-Zero, plain decongestants like Mucinex, Bouillon or clear soups, lots of Kleenex and avoid solids and dairy products while you are symptomatic. The rest is just common sense.
What are the symptoms of Coronavirus The symptoms of this virus include high fever, respiratory problems, shortness of breath and coughing. In extreme cases, it can even lead to pneumonia, kidney failure and death.To prevent infection from spreading, one should wash hands regularly, cover mouth and nose while coughing and sneezing and eat properly cook meat and eggs."""
raw = raw.lower()
sent_tokens = nltk.sent_tokenize(raw)# converts to list of sentences 
word_tokens = nltk.word_tokenize(raw)# converts to list of words
lemmer = nltk.stem.WordNetLemmatizer()
#WordNet is a semantically-oriented dictionary of English included in NLTK.
def LemTokens(tokens):
    return [lemmer.lemmatize(token) for token in tokens]
remove_punct_dict = dict((ord(punct), None) for punct in string.punctuation)

def LemNormalize(text):
    return LemTokens(nltk.word_tokenize(text.lower().translate(remove_punct_dict)))
GREETING_INPUTS = ("hello", "hi", "greetings", "sup", "what's up","hey", "hi Babe", "how are you?")
GREETING_RESPONSES = ["hi", "hey", "*nods*", "hi there", "hello", "I am glad! You are talking to me","Thanks for asking"]
def greeting(sentence):
 
    for word in sentence.split():
        if word.lower() in GREETING_INPUTS:
            return random.choice(GREETING_RESPONSES)
def response(user_response):
    robo_response=''
    sent_tokens.append(user_response)
    TfidfVec = TfidfVectorizer(tokenizer=LemNormalize, stop_words='english')
    tfidf = TfidfVec.fit_transform(sent_tokens)
    vals = cosine_similarity(tfidf[-1], tfidf)
    idx=vals.argsort()[0][-2]
    flat = vals.flatten()
    flat.sort()
    req_tfidf = flat[-2]
    if(req_tfidf==0):
        robo_response=robo_response+"I am sorry! I don't understand you"
        return robo_response
    else:
        robo_response = robo_response+sent_tokens[idx]
        return robo_response
flag=True
print("ROBO: My name is Robo. I will answer your queries about Chatbots. If you want to exit, type Bye!")
while(flag==True):
    user_response = input()
    user_response=user_response.lower()
    if(user_response!='bye'):
        if(user_response=='thanks' or user_response=='thank you' ):
            flag=False
            print("ROBO: You are welcome..")
        else:
            if(greeting(user_response)!=None):
                print("ROBO: "+greeting(user_response))
            else:
                print("ROBO: ",end="")
                print(response(user_response))
                sent_tokens.remove(user_response)
    else:
        flag=False
        print("ROBO: Bye! take care..")