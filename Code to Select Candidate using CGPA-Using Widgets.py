
# coding: utf-8

# In[6]:


import ipywidgets as widgets


# In[10]:


from ipywidgets import interact, interactive, fixed, interact_manual


# In[7]:


danger=widgets.IntProgress(
    value=2,
    min=0,
    max=10,
    step=1,
    description='Status:',
    bar_style='Warning', # 'success', 'info', 'warning', 'danger' or ''
    orientation='horizontal'
)

success=widgets.IntProgress(
    value=10,
    min=0,
    max=10,
    step=1,
    description='Status:',
    bar_style='success', # 'success', 'info', 'warning', 'danger' or ''
    orientation='horizontal'
)

Warning=widgets.IntProgress(
    value=6,
    min=0,
    max=10,
    step=1,
    description='Status:',
    bar_style='Warning', # 'success', 'info', 'warning', 'danger' or ''
    orientation='horizontal'
)


# In[8]:


def myfunc():
    Candidate=input('Enter Candidates Name: ')
    CGPA=int(input('Enter your Degree CGPA: '))
    
    if CGPA <=3:
        
        display(danger)
        print(f'{Candidate}, Not Selected!')
        
    elif CGPA in range(4,7):
        display(warning)
        print('On Hold!')
        
    else:
        display(success)
        print(f'Candidate : {Candidate} Selected')
        
    print(f' candidate {Candidate} has CGPA {CGPA}! ')


# In[14]:


@interact(Candidate=['Amit','B','X','Y'],CGPA=(0,10,1))
def myfunc(Candidate,CGPA):
    #Candidate=input('Enter Candidates Name: ')
    #CGPA=int(input('Enter your Degree CGPA: '))
    
    if CGPA <=3:
        
        display(danger)
        print(f'{Candidate}, Not Selected!')
        
    elif CGPA in range(4,7):
        display(Warning)
        print('On Hold!')
        
    else:
        display(success)
        print(f'Candidate : {Candidate} Selected')
        
    print(f' candidate {Candidate} has CGPA {CGPA}! ')

