#!/usr/bin/env python
# coding: utf-8

# In[1]:


url = 'https://www.gutenberg.org/files/2701/2701-h/2701-h.htm'


# In[2]:


import requests


# In[3]:


r = requests.get(url)
type(r)


# In[4]:


get_ipython().run_line_magic('pinfo', 'requests')


# In[5]:


html = r.text
print(html)


# In[7]:


# Mengimport BeautifulSoup dari bs4
from bs4 import BeautifulSoup

# Membuat Objek BeautifulSoup dari HTML
soup = BeautifulSoup(html,"html5lib")
type(soup)


# In[8]:


soup.title


# In[9]:


soup.title.string


# In[10]:


soup.findAll('a'[:8])


# In[11]:


text = soup.get_text()
print(text)


# In[12]:


import nltk
nltk.download()


# In[13]:


# Import paket regex
import re

# Definisikan sentence
sentence = 'peter piper a peck of pickled peppers'

# Definisikan regex
ps = 'p\w+'

# Mencari semua kata di sentence yang cocok dengan regex kemudian cetak
re.findall(ps, sentence)


# In[14]:


re.findall('\w+', sentence)


# In[16]:


tokens = re.findall('\w+', text)
tokens [:8]


# In[18]:


# Import RegexpTokenizer dari nltk.tokenize
from nltk.tokenize import RegexpTokenizer

# Buat tokenizer
tokenizer = RegexpTokenizer ('\w+')

# Buat tokens
tokens = tokenizer.tokenize (text)
tokens [:8]


# In[19]:


# Menginstalisasi ke dalam list
words = []

# Loop dari list tokens dan buat huruf kecil/lower case
for word in tokens:
    words.append(word.lower())
    
# Cetak beberapa
word[:8]


# In[20]:


# Import modul nltk
import nltk
nltk.download('stopwords')

# Get English stopword and print some of them
sw = nltk.corpus.stopwords.words('english')
sw [:5]


# In[21]:


# Menginisialisasi ke dalam list
words_ns = []

# Tambahkan ke word_ns semua kata yang ada dalam words tetapi tidak dalam sw
for word in words:
    if word not in sw : 
        words_ns.append(word)
        
# Cetak beberapa
words_ns[:5]


# In[23]:


# Import datavis libraries
import matplotlib.pyplot as plt
import seaborn as sns

# Figure inline dan setting style visualisasi
get_ipython().run_line_magic('matplotlib', 'inline')
sns.set

# Buat frekuensi distribusi dan plot 25 kata
freqdist1 = nltk.FreqDist(words_ns)
freqdist1.plot(25)


# In[ ]:




