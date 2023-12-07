#!/usr/bin/env python
# coding: utf-8

# In[7]:


import requests

# Set the URL for the Flask server
url = 'http://127.0.0.1:5000/predict'

# Sample input data
sample_data = {'features': [1.4, 1.2, 1.3, 0.5]}

# Make a POST request to the server
response = requests.post(url, json=sample_data)

# Print the server's response
print(response.json())

