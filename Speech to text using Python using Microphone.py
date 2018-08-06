
# coding: utf-8

# In[ ]:


#Speech to text using Python using Microphone

import speech_recognition as sr

r = sr.Recognizer()
    
mic = sr.Microphone()

with mic as source:
    r.adjust_for_ambient_noise(source,duration=0.5)# Eliminating Background Noise
    audio = r.listen(source)
    
r.recognize_google(audio)

