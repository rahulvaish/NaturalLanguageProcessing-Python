
# coding: utf-8

# In[14]:


from chatterbot import ChatBot


# In[15]:


from chatterbot.trainers import ListTrainer


# In[16]:


chatbot = ChatBot('HIST-2')


# In[17]:


chatbot.set_trainer(ListTrainer)


# In[18]:


data = open('D://DataScienceCollection//NLP Docs//ChatterbotInput.txt').read()


# In[19]:


conversations = data.strip().split('\n')
chatbot.train(conversations)


# In[20]:


chatbot.get_response('Who was the son of Humayun')


# In[21]:


chatbot.get_response('Who was the father of Akbar')

