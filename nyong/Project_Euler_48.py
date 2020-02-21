#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Project 48


# In[2]:


def main():
    """Main Program"""
    total = 0
    tally = ''
    for i in range(1, 1001):
        total = total + (i ** i)
    x = str(total)
    y = len(x) - 10
    s = x[y:]
    print ("Project Euler 48 Solution = ", s)
     
if __name__ == '__main__':
    main()


# In[ ]:




