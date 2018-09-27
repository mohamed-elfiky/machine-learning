
# coding: utf-8

# In[1]:


from sklearn import tree


# In[2]:


X  = [[181, 80, 44], [177, 70, 43], [160, 60, 38], [154, 54, 37], [166, 65, 40],
     [190, 90, 47], [175, 64, 39],
     [177, 70, 40], [159, 55, 37], [171, 75, 42], [181, 85, 43]]

Y  = ['male', 'male', 'female', 'female', 'male', 'male', 'female', 'female',
      'female', 'male', 'male']


# In[5]:


clf = tree.DecisionTreeClassifier()
clf = clf.fit(X,Y)


# In[6]:


prediction=clf.predict([[190,77,44]])
print(prediction)

