#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd 
df = pd.read_csv(r'C:\Users\aaliy\OneDrive\Desktop\Phishing Detector\Backend\data\merged_urls.csv')
#it just says ki go ek level upar to access the csv file


# In[2]:


import re
from urllib.parse import urlparse
def extract_features(url):
    feature={}
    
    #Feature 1
    if re.match(r"http[s]?://\d+\.\d+\.\d+\.\d+",url):
        feature['has_ip']=1
    else:
        feature['has_ip']=0
    r'''we check if the url consists of an IP address
    \d+ => more than one number '''
    
    #Feature 2
    feature["url_len"]=len(url)
    '''checking the length of the url as lengthy url are often phishy'''
    
    #Feature 3
    feature["has_@"]=int("@" in url)
    '''it checks if url contains @ and then converts the answer to 0 or 1 so as to use it later'''
    
    #Feature 4
    feature["has_//"]=1 if url.find("//", 8) != -1 else 0
    '''checks if the url has // after the 8th index that is after http://'''
    
    #Feature 5
    domain=urlparse(url).netloc
    feature["has-"]=int('-' in domain)
        
    #Feature 6
    protocol=urlparse(url).scheme
    feature["has_https"]=int(protocol=="https")
        
    #Feature 7
    domain=urlparse(url).netloc
    feature["has_http_in_domain"]=int('http' in domain)
    
    #Feature 8
    feature["numof_dots"] = url.count(".")
    
    return feature


# In[3]:


features = df['url'].apply(extract_features).tolist()
features_df = pd.DataFrame(features)
features_df['label'] = df['label']


# In[4]:


X=features_df.drop('label', axis=1)
y=features_df['label']


# In[ ]:


from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, confusion_matrix

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.33, random_state=42)
model=LogisticRegression()
model.fit(X_train, y_train)
y_pred = model.predict(X_test)
print("Accuracy:", accuracy_score(y_test, y_pred))
print("Confusion Matrix:\n", confusion_matrix(y_test, y_pred, labels=[0, 1]))


# In[ ]:


import joblib
joblib.dump(model, 'phishing_model.pkl')

