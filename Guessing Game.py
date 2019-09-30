#!/usr/bin/env python
# coding: utf-8

# ## Create a Guessing Game

# In[1]:


import random


# In[2]:


true_number = random.randint(1, 49)


# In[3]:


true_number


# In[4]:


guess_number = int(input("Enter your guess between 1 and 49: "))


# In[5]:


guess_number


# In[ ]:


while True:
    if guess_number == true_number:
        print('YOU ARE RIGHT! GOOD JOB!')
        break
    
    elif guess_number < true_number:
        print('YOUR GUESS IS LOW, TRY AGAIN')
        guess_number = int(input("Enter your guess between 1 and 49: "))
              
    elif guess_number > true_number:
        print('YOUR GUESS IS HIGH, TRY AGAIN')
        guess_number = int(input("Enter an integer from 1 and 49: "))
  


# In[ ]:




