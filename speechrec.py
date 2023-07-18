import speech_recognition as sr 
import paramiko as par 
from os import startfile
from datetime import datetime
import webbrowser as w
#import pywhatkit as p
import pandas as pd
r = sr.Recognizer()  
r = sr.Recognizer()
file=open("C:/notes.txt","w") 
def fun():
    with sr.Microphone() as source:  
        print("Talk...") 
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source)  
    try:  
        return r.recognize_google(audio)  
    except sr.UnknownValueError:  
        return 'cant understand'
    except sr.RequestError as e:  
        print("Sphinx error; {0}".format(e))
def fun1(k,a):
    for i in a:
        if(k==i):
            return 1
    return 0
while True:
    k=fun()
    print("How can I help you??")
    #k='hello'
    print('You said: ',k)
    if(k=='stop' or k=='stop stop' or 'stop' in k or 'bye' in k or 'top' in k):
        break
    if('play' in k):
        k=k.replace('play','',1)
        p.playonyt(k)
    if('open up' in k):
        k=k.replace('open up','',1)
        w.open('http://'+k+'.com')
    if('open notes' in k):
        startfile('C:/notes.txt')
    elif('hi bro' in k or 'hi' in k):
        print('\nMB: How are you....!')
    elif('well' in k or 'fine' in k):
        print('\nMB: Good to hear')
    elif('I want to buy' in k or 'buy' in k):
        k=k.replace('I want to buy ','',1)
        w.open('https://www.amazon.in/s?k='+k+'&s=price-asc-rank&qid=1608278581&ref=sr_st_price-asc-rank')
        w.open('https://www.flipkart.com/search?q='+k+'&as=on&as-show=on&otracker=AS_Query_TrendingAutoSuggest_1_0_na_na_na&otracker1=AS_Query_TrendingAutoSuggest_1_0_na_na_na&as-pos=1&as-type=TRENDING&suggestionId=mobiles&requestId=ced0112e-5c58-448b-9714-3ed688ba8beb')
    elif('what is' in k or 'search for' in k or 'tell me about' in k):
        k=k.replace('what is','',1)
        k=k.replace('search for','',1)
        w.open('https://www.google.com/search?q='+k+'&oq=enc&aqs=chrome.0.69i59l2j69i57j0i20i263i433j0i433j69i60l3.1092j0j4&sourceid=chrome&ie=UTF-8')
    elif('weather' in k):
        w.open('https://www.google.com/search?q='+'weather'+'&oq=enc&aqs=chrome.0.69i59l2j69i57j0i20i263i433j0i433j69i60l3.1092j0j4&sourceid=chrome&ie=UTF-8')