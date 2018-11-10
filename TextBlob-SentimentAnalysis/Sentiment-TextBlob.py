
# coding: utf-8

# In[35]:


import nltk;


# In[36]:


from textblob import TextBlob


# In[37]:


blob1 = TextBlob("I hate Monday")


# In[38]:


print(format(blob1.sentiment))


# In[39]:


blob2 = TextBlob("I love California")


# In[40]:


print(format(blob2.sentiment))


# In[41]:


blob3 = TextBlob("I hate Monday but I love California")


# In[42]:


print(format(blob3.sentiment))


# In[43]:


blob4= TextBlob("I love Monday but I hate Monday")


# In[44]:


print(format(blob4.sentiment))


# In[45]:


blob5 = TextBlob("Miss Universe is beautiful")


# In[46]:


print(format(blob5.sentiment))

