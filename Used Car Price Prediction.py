#!/usr/bin/env python
# coding: utf-8

# In[8]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import r2_score


# In[23]:


car_dataset=pd.read_csv("car data.csv")
car_dataset.head()


# In[22]:


car_dataset.shape


# In[62]:


car_dataset.columns


# In[21]:


car_dataset.info()


# In[20]:


car_dataset.isnull().sum()


# In[19]:


print(car_dataset.Fuel_Type.value_counts())


# In[18]:


print(car_dataset.Seller_Type .value_counts())


# In[8]:


print(car_dataset.Transmission.value_counts())


# In[15]:


car_dataset=car_dataset.drop(columns="Car_Name")


# In[16]:


car_dataset.head()


# In[13]:


car_dataset.head()


# In[24]:


car_dataset.select_dtypes(include="object").columns


# In[74]:


final_dataset=pd.get_dummies(data=car_dataset,drop_first=True)
final_dataset


# In[28]:


y=car_dataset["Selling_Price"]


# In[29]:


x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.2,random_state=0)


# In[30]:


x_train.shape


# In[31]:


x_test.shape


# In[72]:


regressor=LinearRegression()
regressor.fit(x_train,y_train)


# In[42]:


regressor.intercept_


# In[45]:


regressor.coef_


# In[50]:


y_pred=regressor.predict(x_test)


# In[34]:


y_pred


# In[66]:


r2_score(y_test,y_pred)


# In[64]:


regressor.score


# In[65]:


single_obs=[[8.50,4500,0,5,1,0,0,1]]


# In[67]:


regressor.predict(single_obs)


# In[64]:


single_obs1=[[5.59,2700,0,7,0,1,0,1]]
regressor.predict(single_obs1)


# In[46]:


x=["Selling_Price"]
y=y_pred
plt.scatter(x,y)


# In[ ]:




