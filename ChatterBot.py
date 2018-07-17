
# coding: utf-8

# In[31]:


from chatterbot import ChatBot


# In[32]:


from chatterbot.trainers import ListTrainer


# In[33]:


chatbot = ChatBot('HIST')


# In[34]:


chatbot.set_trainer(ListTrainer)


# In[35]:


chatbot.train(['Who build the Taj Mahal', 'Emperor Shah Jahan'])


# In[36]:


chatbot.get_response('Who build the Taj Mahal')


# In[37]:


chatbot.get_response('Who build the Bada Imambara in Lucknow')


# In[38]:


chatbot.train(['Who build the Bada Imambara in Lucknow', 'Nawab Asaf'])


# In[39]:


chatbot.get_response('Who build the Bada Imambara in Lucknow')


# In[40]:


chatbot.get_response('Who build the Taj Mahal')


# In[41]:


chatbot.get_response('Who build the Bada Imambara in Lucknow ?')


# In[42]:


chatbot.get_response('Bada Imambara')


# In[43]:


chatbot.get_response('When was Bada Imambara build')


# In[44]:


chatbot.get_response('When was Taj Mahal build')


# In[30]:


#chatbot.storage.drop()


# In[45]:


chatbot.train(['When was Taj Mahal build' , '1648'])


# In[46]:


chatbot.get_response('When was Taj Mahal build')


# In[47]:


chatbot.get_response('Taj Mahal')


# In[48]:


chatbot.get_response('In which year Taj Mahal was build')


# In[49]:


chatbot.get_response('Who build the Taj Mahal')

