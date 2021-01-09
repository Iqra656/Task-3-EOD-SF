#!/usr/bin/env python
# coding: utf-8

# # Data Science and Business Analytics
# ## Task-3 Exploratory Data Analysis- Retail
# # By: Iqra Malik
# ## Problem statement :As a business manager, try to find out the weak areas where you can work to make more profit. 

# In[17]:


#Importing the Libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt 
get_ipython().run_line_magic('matplotlib', 'inline')
import seaborn as sns 


# In[22]:


#Reading Dataset
df = pd.read_csv("C:/Users/Imran/Desktop/My Projects/SampleSuperstore.csv")
df.head()


# In[23]:


#Total no. of rows and column in a Dataset 
df.shape


# In[138]:


#For data information
df.info()


# In[139]:


#Describing data
df.describe()


# In[140]:


#To check is there any null value
df.isnull().sum()


# In[142]:


#Show column names
df.columns


# In[143]:


#check uniqueness
df.nunique()


# In[144]:


#Check sum of the duplicate value
df.duplicated().sum()


# In[145]:


#drop duplicate value
df.drop_duplicates(keep = 'first',inplace = True)


# In[39]:


#For confirmation
df.duplicated().sum()


# In[41]:


#Drop the column which doesn't necessary
df=df.drop(["Country","Postal Code"],axis=1)
df.head()


# #### Plotting Heatmap which shows the correlation between Sales, Discount,Quantity,Profit

# In[43]:


fig= plt.figure(figsize=(10,6))
sns.heatmap(df.corr(),linewidth=1,annot=True)


# # Exploratory Data Analysis
# 
# #### Plot shows the relationship between Sales and Profit

# In[44]:


sns.jointplot(x='Sales',y='Profit',data=df)


# #### Plot shows the no. of categories where Sales done

# In[54]:


sns.countplot(x='Category',data=df)


# In[68]:


#Plot the Sub-Categories
plt.figure(figsize=(15,6))
sns.countplot(x='Sub-Category',data=df,palette="BrBG")


# #### It Shows the different ShipMode 

# In[62]:


sns.countplot(x="Ship Mode",data=df)


# #### We can see the highest no. of Sales done in Standard Class

# ## Pairplot analyse to each Column
# ### 1.Based on Region

# In[111]:


sns.pairplot(df,hue='Region')


# ### 2.Based on Category

# In[100]:


sns.pairplot(df,hue='Category')


# ### Califonia and New York has highest no. of Sales Done

# In[83]:


plt.figure(figsize=(10,6))
sns.countplot(x='State',data=df)
plt.xticks(rotation=90)
plt.grid()


# #### Plotting the histogram showing Discount, Profit,Quantity,Sales 

# In[146]:


df.hist(edgecolor="Black",linewidth=1.4,figsize=(10,10))
fig=plt.gcf
plt.show()


# ### More number of Sales done in Consumer segment with highest profit 

# In[147]:


df.groupby('Segment')[['Profit','Sales']].sum().plot.bar(color=['yellow','black'],figsize=(8,6))
plt.ylabel('Profit and Sales')
plt.show()


# In[112]:


df['Segment'].value_counts()


# In[122]:


df_segment=df.groupby(['Segment'])['Sales','Discount','Profit'].mean()
df_segment


# In[116]:


df[df['Segment']=='Consumer'].Profit.sum()


# In[119]:


df[df['Segment']=='Corporate'].Profit.sum()


# In[118]:


df[df['Segment']=='Home Office'].Profit.sum()


# In[123]:


df_segment.plot.pie(subplots=True,labels=df_segment.index,autopct="%1.2f%%",figsize=(18,20))


# ### We can see that Sales and Profit both are more in Home office Segment 
# ### Discount is almost same in Corporate and Consumer segment

# In[96]:


df.groupby('Sub-Category')[['Profit','Sales']].sum().plot.bar(color=['purple','red'],figsize=(8,6))
plt.ylabel('Profit and Sales')
plt.show()


# In[98]:


df.groupby('Ship Mode')[['Profit','Sales']].sum().plot.bar(color=['Orange','black'],figsize=(8,6))
plt.ylabel('Profit and Sales')
plt.show()


# # Profit Analyzation based on ShipMode

# In[105]:


df_shipmode=df.groupby(['Ship Mode'])['Sales','Discount','Profit'].mean()
df_shipmode


# In[106]:


df[df['Ship Mode']== 'Standard Class'].Profit.sum()


# In[107]:


df[df['Ship Mode']== 'First Class'].Profit.sum()


# In[108]:


df[df['Ship Mode']== 'Second Class'].Profit.sum()


# In[110]:


df_shipmode.plot.pie(subplots=True,labels=df_shipmode.index,autopct="%1.2f%%",figsize=(18,20))


# ## We can see that Profit is more in first class
# ## Discount is more in first class
# ## Sales are more in first day

# # Profit analyzation based on City

# In[148]:


df['City'].unique()


# In[149]:


df['City'].value_counts()


# In[150]:


fig,ax=plt.subplots(figsize=(30,8))
sns.countplot(df['City'].head(100),ax=ax)


# In[151]:


df_city=df.groupby(['City'])['Sales','Discount','Profit'].mean()
df_city


# ### Sorting th cities with respect to profit in descenting order

# In[152]:


df_city=df_city.sort_values("Profit",ascending=False)
df_city.head(10)


# ### Least Profit giving cities 

# In[153]:


df_city.tail(10)


# ### Plot profit discount,Sales of Top 20 cities

# In[154]:


df_city['Profit'].head(20).plot(kind='bar',figsize=(15,5),color='Green')
plt.title("Citywise analysis of profit")


# ### Low Profit cities

# In[155]:


df_city['Profit'].tail(20).plot(kind='bar',color='red',figsize=(15,5))
plt.title("City wise analysis of Loss")


# ## Category wise analysis of profit

# In[157]:


df['Category'].unique()


# In[158]:


df_category=df.groupby(['Category'])['Sales','Discount','Profit'].mean()
df_category


# In[159]:


df_category.plot.pie(subplots=True,labels=df_category.index,autopct="%1.2f%%",figsize=(18,20))


# ### Highest Profit and Sales in Technology
# ### Second Highest Sales in Furniture but 37.93% but its profit is too less
# ### As highest amount of discount is given in furniture

# # Summary

# ### Sales and Profit are moderately correlated
# ### Quantity and Profit are less moderatey correlated
# ### Discount and Profit are negatively correlated
# ### Furniture has less profit mainly because of huge discount on tables
# ### State ohlo: Lowest profit
# ### State Vermont : Highest Profit
# ## Out of total profit 73% is from Technology

# # Thank you
