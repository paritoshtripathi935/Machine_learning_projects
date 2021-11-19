#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Load EDA Pkgs
import pandas as pd
import neattext.functions as nfx


# In[2]:


# Load ML/Rc Pkgs
from sklearn.feature_extraction.text import CountVectorizer,TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity,linear_kernel


# In[3]:


df = pd.read_csv("/home/paritosh/Desktop/Savo/Data/Programming_courses.csv")


# In[4]:


df.head()


# In[5]:


dir(nfx)


# In[6]:


# Clean Text:stopwords,special charac
df['clean_course_title'] = df['Title'].apply(nfx.remove_stopwords)


# In[7]:


# Clean Text:stopwords,special charac
df['clean_course_title'] = df['clean_course_title'].apply(nfx.remove_special_characters)


# In[8]:


df[['Title','clean_course_title']]


# In[9]:


# Vectorize our Text
count_vect = CountVectorizer()
cv_mat = count_vect.fit_transform(df['clean_course_title'])


# In[10]:


# Sparse
cv_mat


# In[11]:


# Dense
cv_mat.todense()


# In[12]:


df_cv_words = pd.DataFrame(cv_mat.todense(),columns=count_vect.get_feature_names())


# In[13]:


# Cosine Similarity Matrix
cosine_sim_mat = cosine_similarity(cv_mat)


# In[14]:


cosine_sim_mat


# In[15]:


df.head()


# In[16]:


# Get Course ID/Index
course_indices = pd.Series(df.index,index=df['Title']).drop_duplicates()


# In[17]:


df.Title[1]


# In[18]:


idx = course_indices['A deep understanding of deep learning (with Python intro)']


# In[19]:


scores = list(enumerate(cosine_sim_mat[idx]))


# In[20]:


# Sort our scores per cosine score
sorted_scores = sorted(scores,key=lambda x:x[1],reverse=True)


# In[21]:


# Selected Courses Indices
selected_course_indices = [i[0] for i in sorted_scores[1:]]


# In[22]:


# Selected Courses Scores
selected_course_scores = [i[1] for i in sorted_scores[1:]]


# In[23]:


recommended_result = df['Title'].iloc[selected_course_indices]


# In[24]:


rec_df = pd.DataFrame(recommended_result)


# In[25]:


rec_df.head()


# In[26]:


def recommend_course(title,num_of_rec=10):
    # ID for title
    idx = course_indices[title]
    # Course Indice
    # Search inside cosine_sim_mat
    scores = list(enumerate(cosine_sim_mat[idx]))
    # Scores
    # Sort Scores
    sorted_scores = sorted(scores,key=lambda x:x[1],reverse=True)
    # Recomm
    selected_course_indices = [i[0] for i in sorted_scores[1:]]
    selected_course_scores = [i[1] for i in sorted_scores[1:]]
    result = df['Title'].iloc[selected_course_indices]
    rec_df = pd.DataFrame(result)
    rec_df['similarity_scores'] = selected_course_scores
    return rec_df.head(num_of_rec)


# In[27]:


recommend_course("Nonprofit Financial Stewardship Webinar: Introduction to Accounting and Financial Statements",20)


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




