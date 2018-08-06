
# coding: utf-8

# In[ ]:


#pip install pypiwin32
#conda install pypiwin32
import win32com.client
speaker = win32com.client.Dispatch("SAPI.SpVoice")

def audio():
    s = str(input('Enter the text'))
    speaker.Speak(s)

