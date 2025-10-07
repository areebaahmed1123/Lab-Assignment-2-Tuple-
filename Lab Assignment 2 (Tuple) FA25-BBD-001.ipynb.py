#!/usr/bin/env python
# coding: utf-8

# In[2]:


#Task 1: Basic Creation and Access
my_info=('Areeba', 19, 5.10)
print(my_info)
print(my_info[1])


# In[8]:


#Task 2: Single-Item Tuple
single_day=("Monday",)
print(type(single_day))


# In[9]:


#Task 3: Negative Indexing
planets=('Mercury', 'Venus', 'Earth', 'Mars', 'Jupiter')
print(planets[-1])
print(planets[-3])


# In[10]:


#Task 4: Tuple Concatenation
front_numbers=(1, 2, 3)
back_numbers=(4, 5, 6)
combined_numbers= front_numbers + back_numbers
print(combined_numbers)


# In[19]:


#Task 5: Tuple Repetition
icon = ('🌟')
ratings = icon*3
print(ratings)


# In[12]:


#Task 6: Immutability Test
status=('pending', 'processing', 'completed')
status[0]='failed'
#A 'TypeError' occurs due to tuples being immutable. You cannot add or remove elements from a Tuple.


# In[18]:


#Task 7: Tuple Slicing
given_data=(10, 20, 30, 40, 50, 60, 70)
new_tuple= given_data[2:5]
print(new_tuple[0:2])


# In[21]:


#Task 8: Counting Elements
results=('pass', 'fail', 'pass', 'pass', 'defer', 'pass' )
print(results.count('pass'))
print(results.index('defer'))

